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


## ניצור create table: 
- Create Tables Script  
  [View create_tables.sql](./createtTables.sql)

CREATE TABLE DRIVER
(
  DriverID INT NOT NULL,
  FirstName VARCHAR(20) NOT NULL,
  LastName VARCHAR(20) NOT NULL,
  Phone VARCHAR(11) NOT NULL,
  LicenseNumber INT NOT NULL,
  LicenseType VARCHAR(5) NOT NULL,
  HireDate DATE NOT NULL,
  PRIMARY KEY (DriverID),
  UNIQUE (LicenseNumber)
);

CREATE TABLE VEHICLE
(
  VehicleID INT NOT NULL,
  LicensePlate INT NOT NULL,
  VehicleType VARCHAR(20) NOT NULL,
  Capacity INT NOT NULL,
  Manufacturer VARCHAR(20) NOT NULL,
  Model INT NOT NULL,
  Year INT NOT NULL,
  PRIMARY KEY (VehicleID),
  UNIQUE (LicensePlate)
);

CREATE TABLE TRIP
(
  TripID INT NOT NULL,
  DepartureLocation VARCHAR(20) NOT NULL,
  Destination VARCHAR(20) NOT NULL,
  DepartureTime TIMESTAMP NOT NULL,
  Status BOOLEAN NOT NULL,
  DriverID INT NOT NULL,
  VehicleID INT NOT NULL,
  PRIMARY KEY (TripID),
  FOREIGN KEY (DriverID) REFERENCES DRIVER(DriverID),
  FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID)
);

CREATE TABLE INSURANCE
(
  InsuranceID INT NOT NULL,
  InsuranceCompany VARCHAR(15) NOT NULL,
  PolicyNumber INT NOT NULL,
  StartDate DATE NOT NULL,
  EndDate DATE NOT NULL,
  Cost NUMERIC(10,2) NOT NULL,
  VehicleID INT NOT NULL,
  PRIMARY KEY (InsuranceID),
  FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID),
  UNIQUE (PolicyNumber)
);

CREATE TABLE FUELLOG
(
  FuelLogID INT NOT NULL,
  FuelLogDate DATE NOT NULL,
  FuelAmount NUMERIC(5,2) NOT NULL,
  FuelCost NUMERIC(10,2) NOT NULL,
  FuelStation VARCHAR(20) NOT NULL,
  VehicleID INT NOT NULL,
  DriverID INT NOT NULL,
  PRIMARY KEY (FuelLogID),
  FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID),
  FOREIGN KEY (DriverID) REFERENCES DRIVER(DriverID)
);

CREATE TABLE MAINTENANCE
(
  MaintenanceID INT NOT NULL,
  MaintenanceDate DATE NOT NULL,
  MaintenanceType VARCHAR(20) NOT NULL,
  Cost NUMERIC(10,2) NOT NULL,
  Notes VARCHAR(30) NOT NULL,
  VehicleID INT NOT NULL,
  PRIMARY KEY (MaintenanceID),
  FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID)
);

## ניצור drop table:

DROP TABLE IF EXISTS FUELLOG CASCADE;
DROP TABLE IF EXISTS MAINTENANCE CASCADE;
DROP TABLE IF EXISTS INSURANCE CASCADE;
DROP TABLE IF EXISTS TRIP CASCADE;
DROP TABLE IF EXISTS DRIVER CASCADE;
DROP TABLE IF EXISTS VEHICLE CASCADE;

## ניצור select all: 

-- Select all data from all tables

SELECT * FROM DRIVER;

SELECT * FROM VEHICLE;

SELECT * FROM TRIP;

SELECT * FROM INSURANCE;

SELECT * FROM FUELLOG;

SELECT * FROM MAINTENANCE;




## הערה: insertTables הוא קובץ ארוך ולכן הוא מצורף אבל לא מצוטט פה.

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
<img width="710" height="59" alt="image" src="https://github.com/user-attachments/assets/11c4c648-83a1-4f16-bef0-655ede3845b3" />
<img width="691" height="49" alt="image" src="https://github.com/user-attachments/assets/ed0d5f8e-26cb-44bc-b7ee-ada5aee397e3" />
<img width="690" height="44" alt="image" src="https://github.com/user-attachments/assets/fec08c19-2c75-433e-a791-91589d41a17a" />
<img width="716" height="62" alt="image" src="https://github.com/user-attachments/assets/3b0ee008-fa01-462e-b7ca-3fb11aa570a8" />
<img width="765" height="57" alt="image" src="https://github.com/user-attachments/assets/46f4f2ab-ab93-4973-81e9-25bdd2d95e9f" />


## באמצעות קובץ csv שיוצר על ידי chatGPT:
<img width="741" height="598" alt="image" src="https://github.com/user-attachments/assets/dbee5356-f7b3-4250-a528-de3b962d64c4" />
<img width="668" height="447" alt="image" src="https://github.com/user-attachments/assets/ceed3a1c-bae5-4321-b2b2-624e84ea63e6" />
<img width="673" height="526" alt="image" src="https://github.com/user-attachments/assets/18aaee37-16b3-428e-874f-d1926db6b350" />




## באמצעות סקריפטים בפייתון:
## חיבור למסד הנתונים:
<img width="556" height="174" alt="image" src="https://github.com/user-attachments/assets/9ce3bda9-f5d3-44a8-a342-8e1168c88403" />
## סקריפט לייצור נתונים עבור טבלת driver:
<img width="729" height="767" alt="image" src="https://github.com/user-attachments/assets/4fbd8b46-46b0-4392-a529-91f756d3dea5" />
<img width="700" height="223" alt="image" src="https://github.com/user-attachments/assets/7a1fdcb0-355f-409f-9bd5-0e8bca9bdaeb" />
## סקריפט לייצור נתונים עבור טבלת fuellog:
<img width="683" height="766" alt="image" src="https://github.com/user-attachments/assets/cddd4b49-04a2-42d6-a92f-31d709b3c0ff" />
<img width="732" height="330" alt="image" src="https://github.com/user-attachments/assets/c523d94c-cc8e-4f2a-a878-f1fd95d42bb3" />
## סקריפט לייצור נתונים עבור טבלת insurance:
<img width="677" height="721" alt="image" src="https://github.com/user-attachments/assets/5078879f-c4c1-42c5-8030-f2a917f27d31" />
<img width="743" height="241" alt="image" src="https://github.com/user-attachments/assets/68cdeae1-5d2e-4d7d-8cb7-3f2517f80501" />
## סקריפט לייצור נתונים עבור טבלת maintenance:
<img width="642" height="735" alt="image" src="https://github.com/user-attachments/assets/d796afab-dd5c-4fc3-b0db-4aae6f89e893" />
<img width="727" height="701" alt="image" src="https://github.com/user-attachments/assets/02ce5cd9-c721-4b7b-97f0-22ac0a8f6549" />
## סקריפט לייצור נתונים עבור טבלת trip:
<img width="692" height="755" alt="image" src="https://github.com/user-attachments/assets/39dea141-d7df-42ce-a687-a4e6884c6992" />
<img width="761" height="626" alt="image" src="https://github.com/user-attachments/assets/11bac1e0-5366-4674-af66-a5a82bf9ee6f" />
## סקריפט לייצור נתונים עבור טבלת vehicle:
<img width="761" height="804" alt="image" src="https://github.com/user-attachments/assets/0a35b965-0321-4129-b974-e4cf21027c6d" />
<img width="744" height="229" alt="image" src="https://github.com/user-attachments/assets/89ebe165-524e-48ce-8dfc-ca4a3ea56ab3" />


## באמצעות אתר mockaroo:

<img width="1280" height="532" alt="image" src="https://github.com/user-attachments/assets/867a6f64-22e9-44ea-b6d9-35354d3c5688" />

## גיבוי נתונים:
<img width="1280" height="611" alt="image" src="https://github.com/user-attachments/assets/52217f9c-7c50-4e27-9e80-6cbb1bba87e6" />

## שחזור נתונים:
<img width="1241" height="609" alt="image" src="https://github.com/user-attachments/assets/f22c0d09-5ff4-424d-a0ad-6d7986c8c304" />
