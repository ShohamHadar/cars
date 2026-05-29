---שאילתא שמחשבת את ממוצע עלות תחזוקה לפי סוג רכב + יצרן + שנה
SELECT 
    v.VehicleType,
    v.Manufacturer,
    v.year,
    COUNT(m.MaintenanceID) AS NumOfMaintenances,
    AVG(m.Cost) AS AvgMaintenanceCost
FROM Vehicle v
JOIN Maintenance m ON v.VehicleID = m.VehicleID
GROUP BY v.VehicleType, v.Manufacturer, v.year
ORDER BY AvgMaintenanceCost DESC;

---  שאילתא שמחזירה את רשימת הרכבים עם ביטוח לא בתוקף
SELECT 
    v.VehicleID,
    v.LicensePlate,
    i.EndDate
FROM VEHICLE v
LEFT JOIN INSURANCE i
    ON v.VehicleID = i.VehicleID
WHERE i.EndDate < CURRENT_DATE
   OR i.VehicleID IS NULL
ORDER BY v.VehicleID;


---שאילתא שמחזירה פילוח כמות טיפולי התחזוקה לפי ימי השבוע, מוצג בסדר יורד מהיום העמוס ביותר 
SELECT 
    TO_CHAR(MaintenanceDate, 'Day') AS DayOfWeek, -- מחלץ את שם היום
    COUNT(*) AS MaintenanceCount
FROM MAINTENANCE
GROUP BY DayOfWeek
ORDER BY MaintenanceCount DESC

---שאילתא שמחזירה את רשימת הרכבים שעלות התחזוקה שלהם גבוה מהממוצע הכללי
SELECT 
    v.VehicleID,
    v.VehicleType,
    v.Manufacturer,
    v.Year,
    SUM(m.Cost) AS TotalMaintenanceCost
FROM VEHICLE v
JOIN MAINTENANCE m
    ON v.VehicleID = m.VehicleID
GROUP BY 
    v.VehicleID,
    v.VehicleType,
    v.Manufacturer,
    v.Year
HAVING SUM(m.Cost) > (
    SELECT AVG(vehicle_total.TotalCost)
    FROM (
        SELECT 
            VehicleID,
            SUM(Cost) AS TotalCost
        FROM MAINTENANCE
        GROUP BY VehicleID
    ) AS vehicle_total
)
ORDER BY TotalMaintenanceCost DESC;

---(יותר יעילה) שאילתא שמחזירה רשימה של נהגים שלא ביצעו נסיעה בחודש האחרון
SELECT d.DriverID,
       d.FirstName,
       d.LastName
FROM Driver d
WHERE NOT EXISTS (
    SELECT 1 --בדיקת האם קיימת שורה (לא מחזיר עמודות ספיצפיות)
    FROM Trip t
    WHERE t.DriverID = d.DriverID
      AND t.DepartureTime >= CURRENT_DATE - INTERVAL '1 month'
);
--מה שקורה כאן 

---(פחות יעילה) שאילתא שמחזירה רשימה של נהגים שלא ביצעו נסיעה בחודש האחרון
SELECT DriverID,
	FirstName,
	LastName
FROM Driver
WHERE DriverID NOT IN (
    SELECT DISTINCT DriverID
    FROM Trip
    WHERE DepartureTime >= CURRENT_DATE - INTERVAL '1 month'
);

--- שאילתא יעילה שמחזירה את הרכבים שזמינים השבוע (לא משוריינים לנסיעות)
SELECT 
	v.VehicleID,
	v.Vehicletype,
	v.Capacity
FROM Vehicle v
WHERE NOT EXISTS (
    SELECT 1
    FROM Trip t
    WHERE t.VehicleID = v.VehicleID
      AND t.DepartureTime >= CURRENT_DATE
      AND t.DepartureTime < CURRENT_DATE + INTERVAL '1 week'
);

--- שאילתא פחות יעילה שמחזירה את הרכבים שזמינים השבוע (לא משוריינים לנסיעות)
SELECT 
	VehicleID,
	Vehicletype,
	Capacity
FROM Vehicle
WHERE VehicleID NOT IN (
    SELECT DISTINCT VehicleID
    FROM Trip
    WHERE DepartureTime >= CURRENT_DATE
      AND DepartureTime < CURRENT_DATE + INTERVAL '1 week'
      AND VehicleID IS NOT NULL -- חובה להוסיף כדי שהשאילתה לא תחזור ריקה לגמרי
);

---שאילתא המחשבת עלות ביטוח ממוצע לאוטובוסים לפי חברה בסדר יורד (יעילה)
SELECT 
    insurancecompany, 
    ROUND(AVG(cost)::numeric, 2) AS AvgInsuranceCost
FROM Insurance i
JOIN Vehicle v ON i.VehicleID = v.VehicleID
WHERE v.VehicleType = 'Bus'
GROUP BY insurancecompany
ORDER BY AvgInsuranceCost DESC;

-- שאילתא המחשבת עלות ביטוח ממוצע לאוטובוסים לפי חברה בסדר יורד (פחות יעילה)
SELECT 
    insurancecompany, 
    ROUND(AVG(cost)::numeric, 2) AS AvgInsuranceCost
FROM Insurance
WHERE VehicleID IN (
    SELECT VehicleID 
    FROM Vehicle 
    WHERE VehicleType = 'Bus'
)
GROUP BY insurancecompany
ORDER BY AvgInsuranceCost DESC;

--- שאילתא המחשבת מי הם חמשת הנהגים שביצעו הכי הרבה נסיעות בשנה האחרונה? (שאילתא יעילה)
SELECT 
    d.DriverID,
    d.FirstName,
    d.LastName,
    COUNT(t.TripID) AS NumOfTrips
FROM Driver d
JOIN Trip t ON d.DriverID = t.DriverID
WHERE t.DepartureTime >= CURRENT_DATE - INTERVAL '1 year' -- סינון לשנה האחרונה
GROUP BY d.DriverID, d.FirstName, d.LastName
ORDER BY NumOfTrips DESC
LIMIT 5;


---מי הם חמשת הנהגים שביצעו הכי הרבה נסיעות בשנה האחרונה? (שאילתא פחות יעילה)
SELECT 
    d.DriverID,
    d.FirstName,
    d.LastName,
    (
        SELECT COUNT(*)
        FROM Trip t
        WHERE t.DriverID = d.DriverID
          AND t.DepartureTime >= CURRENT_DATE - INTERVAL '1 year'
    ) AS NumOfTrips
FROM Driver d
ORDER BY NumOfTrips DESC
LIMIT 5;

