# cars
# דוח פרויקט שלב א' - מערכת ניהול צי רכבים

## שער
* **מגישות:** שוהם הדר מימון ואורי סלם
* **המערכת:** מערכת לניהול צי רכבים (Vehicle Fleet Management)
* **יחידה נבחרת:** ניהול חברת הסעות

---
### תוכן עניינים
1. [שער](#שער)
2. [מבוא](#מבוא)
3. [מסכי AI Studio](#מסכי-ai-studio)
4. [קישור לאתר AI Studio](#קישור-לאתר-ai-studio)
5. [תרשים ERD](#תרשים-erd)
6. [תרשים DSD](#תרשים-dsd)
7. [ניצור create table](#ניצור-create-table)
8. [ניצור drop table](#ניצור-drop-table)
9. [ניצור select all](#ניצור-select-all)
10. [שיטות להכנסת נתונים](#שיטות-להכנסת-נתונים)
11. [באמצעות פקודות insert](#1-באמצעות-פקודות-insert)
12. [באמצעות קובץ csv שיוצר על ידי chatgpt](#באמצעות-קובץ-csv-שיוצר-על-ידי-chatgpt)
13. [באמצעות סקריפט פייתון](#באמצעות-סקריפט-פייתון)
14. [באמצעות אתר mockaroo](#באמצעות-אתר-mockaroo)
15. [גיבוי נתונים](#גיבוי-נתונים)
16. [שחזור נתונים](#שחזור-נתונים)

## מבוא
מערכת זו נועדה לניהול כולל ואפקטיבי של צי רכבים במסגרת חברת הסעות.
מטרת המערכת היא לספק מעקב מקיף, תפעולי ופיננסי אחר כלל המשאבים המרכזיים של החברה – רכבים ונהגים – במטרה לאפשר תכנון נסיעות יעיל,
להבטיח את תקינות המלאי, ולבצע בקרת עלויות מדויקת. המערכת תהווה את בסיס הנתונים המרכזי לקבלת החלטות ניהוליות ותפעוליות בזמן אמת.

:
המערכת תאפשר ביצוע מגוון שאילתות ודוחות חיוניים לניהול השוטף:
ניהול מלאי וזמינות: הוספה, עדכון וגריעה של רכבים ונהגים מהצי.
דוחות עלויות ותחזוקה: הפקת דוחות חודשיים על עלויות התדלוק והתחזוקה לכל רכב. זיהוי רכבים שדורשים טיפול קרוב או חריגים בצריכת דלק.
בקרת פוליסות: התרעה מראש על ביטוחים שתוקפם עומד לפוג.
פילוח ביצועים: ניתוח עומס עבודה של נהגים (מספר נסיעות, מרחק) ופילוח רווחיות נסיעות.
מעקב תפעולי: שליפת נתונים על נסיעות מתוכננות ליום מסוים, או היסטוריית טיפולים של רכב ספציפי.

--הישויות במערכת:

1. **נהג** - DRIVER
2. **רכב** - VEHICLE
3. **נסיעה** - TRIP
4. **ביטוח** - INSURANCE
5. **יומן תדלוק** - FUELLOG
6. **תחזוקה** -MAINTENANCE

1. נהג (DRIVER)
DriverID: מספר (INT), מפתח ראשי (Primary Key).
FirstName: מחרוזת (VARCHAR)
LastName: מחרוזת (VARCHAR)
Phone: מחרוזת (VARCHAR)
LicenseNumber: מספר (INT), מפתח ייחודי (Unique Key).
LicenseType: מחרוזת (VARCHAR)
HireDate: תאריך (DATE)

2. רכב (VEHICL)
VehicleID: מספר (INT), מפתח ראשי (Primary Key).
LicensePlate: מספר (INT), מפתח ייחודי (Unique Key).
VehicleType: מחרוזת (VARCHAR)
Capacity: מספר (INT)
Manufacturer: מחרוזת (VARCHAR)
Model: מספר (INT)
Year: מספר (INT)
3. נסיעה (TRIP)
TripID: מספר (INT), מפתח ראשי (Primary Key).
DepartureLocation: מחרוזת (VARCHAR)
Destination: מחרוזת (VARCHAR)
DepartureTime: זמן (TIMESTAMP)
Status: בוליאני (BOOLEAN)
DriverID: מספר (INT), מפתח זר (Foreign Key) המקשר לישות נהג.
VehicleID: מספר (INT), מפתח זר (Foreign Key) המקשר לישות רכב.
4. ביטוח (INSURANC)
InsuranceID: מספר (INT), מפתח ראשי (Primary Key).
InsuranceCompany: מחרוזת (VARCHAR)
PolicyNumber: מספר (INT), מפתח ייחודי (Unique Key).
StartDate: תאריך (DATE)
EndDate: תאריך (DATE)
Cost: מספר עשרוני (NUMERIC)
VehicleID: מספר (INT), מפתח זר (Foreign Key) המקשר לישות רכב.
5. יומן תדלוק (FUELLO)
FuelLogID: מספר (INT), מפתח ראשי (Primary Key).
FuelLogDate: תאריך (DATE)
FuelAmount: מספר עשרוני (NUMERIC)
FuelCost: מספר עשרוני (NUMERIC)
FuelStation: מחרוזת (VARCHAR)
VehicleID: מספר (INT), מפתח זר (Foreign Key) המקשר לישות רכב.
DriverID: מספר (INT), מפתח זר (Foreign Key) המקשר לישות נהג.
6. תחזוקה (MAINTENANCE)MaintenanceID: מספר (INT), מפתח ראשי (Primary Key).
MaintenanceDate: תאריך (DATE)
MaintenanceType: מחרוזת (VARCHAR)
Cost: מספר עשרוני (NUMERIC)
Notes: מחרוזת (VARCHAR)
VehicleID: מספר (INT), מפתח זר (Foreign Key) המקשר לישות רכב.

## מסכי AI Studio:

<img width="990" height="646" alt="image" src="https://github.com/user-attachments/assets/f76f0ae7-79c7-4d46-bf2e-71c14ed9377c" />
<img width="984" height="515" alt="image" src="https://github.com/user-attachments/assets/1969d311-54b2-4f11-92b6-375f6632810b" />
<img width="963" height="476" alt="image" src="https://github.com/user-attachments/assets/cd2ffe7a-5100-4002-a4fe-4ba9b8fd54d9" />
<img width="976" height="460" alt="image" src="https://github.com/user-attachments/assets/fba31c55-21d6-4316-a6e6-910a03fb30bf" />
<img width="971" height="470" alt="image" src="https://github.com/user-attachments/assets/5d890271-f164-4ce2-b21e-8a4baa22b75d" />
<img width="980" height="452" alt="image" src="https://github.com/user-attachments/assets/d09351be-84cd-4a0c-a4dd-86defb4aa914" />
<img width="970" height="477" alt="image" src="https://github.com/user-attachments/assets/f1e74819-4474-4b8b-89e0-ceabf5800a08" />

## קישור לאתר AI Studio:
https://ai.studio/apps/a75accd8-0129-4ba7-8b8c-3a59a5ceec80

## תרשים ERD:
<img width="4314" height="1938" alt="image" src="https://github.com/user-attachments/assets/3c61db40-6cf8-4d0b-8a8d-a3512f0b0f03" />


## תרשים DSD:    
<img width="4314" height="1938" alt="image" src="https://github.com/user-attachments/assets/89d7bcdd-1daa-4714-a306-1beb1efc07c1" />

קישור ל  ERDplus:   https://erdplus.com/diagrams/338819


הסבר על הקשרים המופיעים בתרשימים:
<img width="1627" height="182" alt="image" src="https://github.com/user-attachments/assets/61a71623-8708-471f-aff9-c61b54a1d05d" />

להלן הסבר מפורט על הקשרים במערכת:

### 1. מבצע (Driver - TRIP)
הקשר בין הנהג לנסיעה הוא הלב התפעולי של המערכת:
* **סוג הקשר:** רבים-לאחד ($N:1$).
* **הסבר:** כל נסיעה במערכת חייבת להיות משויכת לנהג אחד ספציפי שאחראי עליה. מצד שני, נהג אחד יכול לבצע נסיעות רבות לאורך זמן (היסטוריית נסיעות), אך הוא אינו יכול לבצע יותר מנסיעה אחת באותו זמן נתון.
* **חובה/רשות:**  **חובה** מצד הנסיעה (אין נסיעה ללא נהג) ו**רשות** מצד הנהג (נהג יכול להיות רשום במערכת מבלי שביצע נסיעה עדיין).

### 2. משויך ל- (Vehicle - TRIP)
הקשר המגדיר איזה כלי רכב משמש לכל משימה:
* **סוג הקשר:** רבים-לאחד ($N:1$).
* **הסבר:** כל נסיעה מתבצעת באמצעות רכב אחד בלבד. רכב ספציפי בצי יכול לשמש לנסיעות רבות מאוד במהלך חייו במערכת.
* **חובה/רשות:** **חובה** מצד הנסיעה (חייב רכב כדי לצאת לדרך) ו**רשות** מצד הרכב (רכב יכול להיות במלאי מבלי ששובץ לנסיעה).

### 3. מבוטח (Vehicle - INSURANCE)
קשר המנהל את הצד המשפטי והכלכלי של הצי:
* **סוג הקשר:** אחד-לרבים ($1:N$).
* **הסבר:** רכב אחד יכול להיות קשור למספר פוליסות ביטוח לאורך השנים (ביטוח חובה, מקיף, או חידוש פוליסה שנתית). כל רשומה בטבלת הביטוח מתייחסת לרכב אחד בלבד.
* **חובה/רשות:** **חובה** - המערכת דורשת שכל רכב יהיה מבוטח כדי שיוכל לפעול בבטחה.

### 4. מתחזק (Vehicle - MAINTENANCE)
קשר המעקב אחר תקינות כלי הרכב:
* **סוג הקשר:** אחד-לרבים ($1:N$).
* **הסבר:** עבור רכב אחד נרשמים דוחות תחזוקה רבים (טיפול 10,000, החלפת צמיגים, תיקון תקלה). כל דוח תחזוקה משויך לרכב הספציפי שעבר את הטיפול.
* **חובה/רשות:** **רשות** - ייתכן רכב חדש שטרם עבר טיפול או תיקון, ולכן אין לו רשומות בטבלה זו.

### 5. מתדלק (Vehicle - FUELLOG)
קשר לניטור הוצאות אנרגיה:
* **סוג הקשר:** אחד-לרבים ($1:N$).
* **הסבר:** רכב אחד צובר רשומות תדלוק רבות מאוד לאורך פעילותו. כל פעולת תדלוק ביומן (FuelLog) מתייחסת לרכב אחד בלבד.
* **חובה/רשות:** **רשות** - רכב שטרם תודלק או דווח עליו במערכת.

### 6. רושם תדלוק (Driver - FUELLOG)
קשר המזהה את האחראי על הוצאת הדלק:
* **סוג הקשר:** אחד-לרבים ($1:N$).
* **הסבר:** הנהג הוא זה שמדווח על התדלוק ומבצע אותו בפועל. נהג אחד יכול לבצע תדלוקים רבים עבור רכבים שונים עליהם נסע.
* **חובה/רשות:** **רשות** - מציין שייתכן נהג שטרם ביצע תדלוק המדווח במערכת.

## סקריפטים של SQL:

- Create Tables Script  
📃 [View createTables.sql](./DBProject_8728_2194/שלב%20א/createTables.sql)

- Insert Data Script
📃 [View insertTables.sql](./DBProject_8728_2194/שלב%20א/insertTables.sql)

- Drop Tables Script  
📃 [View dropTables.sql](./DBProject_8728_2194/שלב%20א/dropTables.sql)

- Select All Data Script
📃 [View selectTables.sql](./DBProject_8728_2194/שלב%20א/selectTables.sql)


הטבלאות:
נהג:
<img width="1474" height="388" alt="צילום מסך 2026-03-30 231132" src="https://github.com/user-attachments/assets/4b78a100-768b-4a37-aba4-fd78e557a0ec" />

רכב:

<img width="1470" height="386" alt="צילום מסך 2026-03-30 231156" src="https://github.com/user-attachments/assets/80c33721-2326-449f-b79f-6ee0f566ba2d" />

נסיעה: 

<img width="1477" height="427" alt="צילום מסך 2026-03-30 231228" src="https://github.com/user-attachments/assets/fff9bbc9-7b0a-4bdb-93d5-350d55c2fb96" />


ביטוח:

<img width="1486" height="446" alt="צילום מסך 2026-03-30 231244" src="https://github.com/user-attachments/assets/4cb0fc01-097e-4257-856f-3da6dc6e2682" />


תדלוקים:

<img width="1482" height="420" alt="צילום מסך 2026-03-30 231301" src="https://github.com/user-attachments/assets/fb1a7772-7da7-4e25-8699-0f5451d4b9d6" />

תחזוקה:

<img width="1476" height="427" alt="צילום מסך 2026-03-30 231316" src="https://github.com/user-attachments/assets/353d6bb6-bbd3-4e7c-861c-68f3d2259774" />


ניצור DSD:

<img width="662" height="427" alt="צילום מסך 2026-03-30 230047" src="https://github.com/user-attachments/assets/474a7e01-393a-4bab-b21b-c6f1ed32d160" />

## שיטות להכנסת נתונים:

## 1: באמצעות פקודות insert: 
- Insert Data Script
📃 [View insertTables.sql](./DBProject_8728_2194/שלב%20א/insertTables.sql)


## באמצעות קובץ csv שיוצר על ידי chatGPT:
📃 [View driver.csv](./DBProject_8728_2194/שלב%20א/DataImportFiles/driver.csv)
📃 [View fuellog.csv](./DBProject_8728_2194/שלב%20א/DataImportFiles/fuellog.csv)
📃 [View insurance.csv](./DBProject_8728_2194/שלב%20א/DataImportFiles/insurance.csv)
📃 [View maintenance.csv](./DBProject_8728_2194/שלב%20א/DataImportFiles/maintenance.csv)
📃 [View trip.csv](./DBProject_8728_2194/שלב%20א/DataImportFiles/trip.csv)
📃 [View vehicle.csv](./DBProject_8728_2194/שלב%20א/DataImportFiles/vehicle.csv)
## באמצעות סקריפטים בפייתון:
## חיבור למסד הנתונים:
📃 [View db.py](./DBProject_8728_2194/שלב%20א/Programing/db.py)
## סקריפט לייצור נתונים עבור טבלת driver:
📃 [View generate_driver.py](./DBProject_8728_2194/שלב%20א/Programing/generate_driver.py)
## סקריפט לייצור נתונים עבור טבלת fuellog:
📃 [View generate_fuellog.py](./DBProject_8728_2194/שלב%20א/Programing/generate_fuellog.py)
## סקריפט לייצור נתונים עבור טבלת insurance:
📃 [View generate_insurance.py](./DBProject_8728_2194/שלב%20א/Programing/generate_insurance.py)
## סקריפט לייצור נתונים עבור טבלת maintenance:
📃 [View generate_maintenance.py](./DBProject_8728_2194/שלב%20א/Programing/generate_maintenance.py)
## סקריפט לייצור נתונים עבור טבלת trip:
📃 [View generate_trip.py](./DBProject_8728_2194/שלב%20א/Programing/generate_trip.py)
## סקריפט לייצור נתונים עבור טבלת vehicle:
📃 [View generate_vehicle.py](./DBProject_8728_2194/שלב%20א/Programing/generate_vehicle.py)


## באמצעות אתר mockaroo:

<img width="1280" height="532" alt="image" src="https://github.com/user-attachments/assets/867a6f64-22e9-44ea-b6d9-35354d3c5688" />

## גיבוי נתונים:
<img width="1280" height="611" alt="image" src="https://github.com/user-attachments/assets/52217f9c-7c50-4e27-9e80-6cbb1bba87e6" />

## שחזור נתונים:
<img width="1241" height="609" alt="image" src="https://github.com/user-attachments/assets/f22c0d09-5ff4-424d-a0ad-6d7986c8c304" />
