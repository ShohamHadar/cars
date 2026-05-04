-- =========================================
-- DELETE (with begin and rollback)
-- =========================================
--מחיקת אוטובסים משנת ייצור נמוכה מ-2019 שאינן משובצות לנסיעות עתידיות וכל הפרטים המשוייכים אליהן
BEGIN;

DELETE FROM vehicle
WHERE vehicletype = 'Bus' 
  AND year < 2019
  AND vehicleid NOT IN (
      -- תת שאילתה לא טרוויאלית המצלבת נתונים עם טבלת הנסיעות
      -- מוודאת שלא נמחק רכב שמשובץ לנסיעה עתידית (גם אם הוא ישן)
      SELECT DISTINCT vehicleid 
      FROM trip
      WHERE status = 'True' 
        AND (
            EXTRACT(YEAR FROM departuretime) > EXTRACT(YEAR FROM CURRENT_DATE)
            OR (
                EXTRACT(YEAR FROM departuretime) = EXTRACT(YEAR FROM CURRENT_DATE) 
                AND EXTRACT(MONTH FROM departuretime) >= EXTRACT(MONTH FROM CURRENT_DATE)
            )
        )
  );

SELECT COUNT(*) FROM vehicle; 

ROLLBACK;

SELECT COUNT(*) FROM vehicle;


--  מחיקת תדלוקים מעל שנה לרכבים שלא עברו טיפול צמיגים  

BEGIN;
DELETE FROM fuellog
WHERE (EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM fuellogdate)) >= 1
  AND vehicleid NOT IN (
      -- תת שאילתה לא טרוויאלית: איתור רכבים שעברו טיפול צמיגים
      SELECT DISTINCT vehicleid
      FROM maintenance
      WHERE maintenancetype = 'Tires'
        AND (
            EXTRACT(YEAR FROM maintenancedate) >= EXTRACT(YEAR FROM CURRENT_DATE) - 1
        )
  );

 ROLLBACK;
 SELECT COUNT(*) FROM fuellog;
 
  
---מחיקת נסיעות בשל התנגשות עם לו"ז תחזוקה

BEGIN;
DELETE FROM trip
USING maintenance m
WHERE trip.vehicleid = m.vehicleid
  AND trip.status = 'True'
  -- השוואת תאריכים מלאה בין הטבלאות (המרה ל-date כדי להתעלם מהשעה)
  AND trip.departuretime::date = m.maintenancedate::date;

ROLLBACK;

SELECT COUNT(*) FROM trip;

-- =========================================
-- UPDATE (with begin and commit)
-- =========================================
--המרת סטטוס נסיעה
BEGIN;

ALTER TABLE trip 
ALTER COLUMN status TYPE VARCHAR(20) 
USING (
    CASE 
        WHEN status = true THEN 'Completed' 
        ELSE 'Planned' 
    END
);

COMMIT;
select tripID, status from trip
--------------------------------------
-- עדכון סטטוס תחזוקה
BEGIN;
UPDATE MAINTENANCE
SET maintenance_status = 'In Progress'
WHERE MaintenanceDate >= CURRENT_DATE - INTERVAL '30 days';

-- 1. בדיקה בתוך הטרנזקציה (מראה את השינוי)
SELECT maintenance_status, COUNT(*) FROM MAINTENANCE GROUP BY maintenance_status;

COMMIT;

-- 2. בדיקה אחרי ה-COMMIT (מראה שהשינוי נשאר אותו דבר!)
SELECT maintenance_status, COUNT(*) FROM MAINTENANCE GROUP BY maintenance_status;

--------------------------------------
-- עדכון עיר לנהגים
BEGIN;
UPDATE Driver 
SET City = (ARRAY['Jerusalem', 'Haifa', 'Ashdod', 'Tel Aviv', 'Eilat', 'Netanya', 'Holon',
'Raanana', 'Tiberias', 'Safed', 'Ashkelon', 'Nazareth', 'Beer Sheva', 'Bat Yam', 'Herzliya', 'Lod', 'Ramat Gan', 'Petah Tikva'])[floor(random() * 18 + 1)];

-- 1. בדיקה בתוך הטרנזקציה
SELECT DriverID, City FROM Driver LIMIT 5;

COMMIT;

-- 2. בדיקה אחרי ה-COMMIT (מראה שהערים נשארו כפי שעודכנו)
SELECT DriverID, City FROM Driver LIMIT 5;

--------------------------------------
-- עדכון משך נסיעה (לפי יעדים)
BEGIN;
UPDATE Trip
SET DurationHours = CASE 
    WHEN (DepartureLocation IN ('Tel Aviv', 'Holon', 'Bat Yam', 'Ramat Gan', 'Petah Tikva', 'Herzliya', 'Raanana') 
          AND Destination IN ('Tel Aviv', 'Holon', 'Bat Yam', 'Ramat Gan', 'Petah Tikva', 'Herzliya', 'Raanana')) THEN 0.75
    WHEN (DepartureLocation IN ('Tel Aviv', 'Jerusalem', 'Ashdod', 'Netanya') 
          AND Destination IN ('Tel Aviv', 'Jerusalem', 'Ashdod', 'Netanya')) THEN 1.5
    ELSE 2.0
END;

-- 1. בדיקה בתוך הטרנזקציה
SELECT TripID, DurationHours FROM Trip LIMIT 5;
COMMIT;
-- 2. בדיקה אחרי ה-COMMIT (מוכיח שהערכים נשמרו)
SELECT TripID, DurationHours FROM Trip LIMIT 5;

--------------------------------------
-- עדכון - שידוך ביטוחים ורכבים
--על מנת להבטיח שלכל רכב יהיה ביטוח אחד בלבד
BEGIN;
--יצירת טבלאות זמניות ליצירת מס׳ סידורי לביטוחים ולרכבים 
WITH RankedVehicles AS (
    SELECT VehicleID, ROW_NUMBER() OVER (ORDER BY VehicleID) as rn FROM Vehicle
),
RankedInsurance AS (
    SELECT InsuranceID, ROW_NUMBER() OVER (ORDER BY InsuranceID) as rn FROM Insurance
)
--קישור בין רכב לביטוח
UPDATE Insurance i
SET VehicleID = rv.VehicleID
FROM RankedVehicles rv
JOIN RankedInsurance ri ON rv.rn = ri.rn
WHERE i.InsuranceID = ri.InsuranceID;

-- 1. בדיקה בתוך הטרנזקציה
SELECT InsuranceID, VehicleID FROM Insurance LIMIT 5;

COMMIT;

-- 2. בדיקה אחרי ה-COMMIT (מראה שהקשר החדש נשמר)
SELECT InsuranceID, VehicleID FROM Insurance LIMIT 5;

--------------------------------------
--עדכון מחיר שעתי לנסיעה לפי סוג רכב
BEGIN;

UPDATE Trip t
SET Price = t.DurationHours * (
    CASE 
        WHEN v.VehicleType = 'Bus' THEN 250 -- 250 ש"ח לשעה לאוטובוס
        WHEN v.VehicleType = 'Minibus' THEN 180
        WHEN v.VehicleType = 'Van' THEN 120
        ELSE 80 -- תעריף ברירת מחדל (למשל למונית)
    END
)
FROM Vehicle v
WHERE t.VehicleID = v.VehicleID
  AND t.DurationHours IS NOT NULL;

-- בדיקה שהנתונים התעדכנו
SELECT TripID, VehicleID, VehicleType, numofpassengers DurationHours, Price FROM Trip LIMIT 10;

COMMIT;

select * from trip