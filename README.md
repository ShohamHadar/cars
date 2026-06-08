# cars
# דוח פרויקט שלב א' - מערכת ניהול צי רכבים

## שער
* **מגישות:** שוהם הדר מימון ואורי סלם
* **המערכת:** מערכת לניהול צי רכבים (Vehicle Fleet Management)
* **יחידה נבחרת:** ניהול חברת הסעות

---
### תוכן עניינים
### שלב א׳:
1. [שער](#שער)
2. [מבוא](#מבוא)
3. [מסכי AI Studio](#מסכי-ai-studio)
4. [קישור לאתר AI Studio](#קישור-לאתר-ai-studio)
5. [תרשים ERD](#תרשים-erd)
6. [תרשים DSD](#תרשים-dsd)
7. [הסבר על הקשרים](#הסבר-על-הקשרים-המופיעים-בתרשימים)
8. [סקריפטים של SQL](#סקריפטים-של-sql)
9. [הטבלאות](#הטבלאות)
10. [שיטות להכנסת נתונים](#שיטות-להכנסת-נתונים)
    10.1 [באמצעות פקודות INSERT](#1-באמצעות-פקודות-insert)
    10.2 [באמצעות קובץ CSV](#באמצעות-קובץ-csv-שיוצר-על-ידי-chatgpt)
    10.3 [באמצעות סקריפטים בפייתון](#באמצעות-סקריפטים-בפייתון)
    10.4 [באמצעות אתר Mockaroo](#באמצעות-אתר-mockaroo)
11. [גיבוי נתונים](#גיבוי-נתונים)
12. [שחזור נתונים](#שחזור-נתונים)

<div dir="rtl">

### שלב ב׳:

1. [שלב ב](#שלב-ב)  
2. [שאילתות select](#שאילתות-select)  
3. [השוואת יעילות בין שתי שאילתות למציאת נהגים שלא ביצעו נסיעה בחודש האחרון](#השוואת-יעילות-בין-שתי-שאילתות-למציאת-נהגים-שלא-ביצעו-נסיעה-בחודש-האחרון)  
4. [השוואת יעילות בין שתי שאילתות למציאת רכבים זמינים השבוע](#השוואת-יעילות-בין-שתי-שאילתות-למציאת-רכבים-זמינים-השבוע)  
5. [השוואת יעילות בין שתי שאילתות לחישוב עלות ביטוח ממוצעת לאוטובוסים לפי חברה](#השוואת-יעילות-בין-שתי-שאילתות-לחישוב-עלות-ביטוח-ממוצעת-לאוטובוסים-לפי-חברה)  
6. [השוואת יעילות בין שתי שאילתות למציאת חמשת הנהגים שביצעו הכי הרבה נסיעות בשנה האחרונה](#השוואת-יעילות-בין-שתי-שאילתות-למציאת-חמשת-הנהגים-שביצעו-הכי-הרבה-נסיעות-בשנה-האחרונה)  
7. [אילוצים](#אילוצים)  
8. [אילוצים בטבלת רכב](#אילוצים-בטבלת-רכב)  
9. [אילוצים בטבלת נהג](#אילוצים-בטבלת-נהג)  
10. [אילוצים בטבלת נסיעה](#אילוצים-בטבלת-נסיעה)  
11. [אילוצים בטבלת תדלוק](#אילוצים-בטבלת-תדלוק)  
12. [אילוצים בטבלת תחזוקה](#אילוצים-בטבלת-תחזוקה)  
13. [אילוצים בטבלת ביטוח](#אילוצים-בטבלת-ביטוח)  
14. [שאילתות delete ושימוש בrollback](#שאילתות-delete-ושימוש-בrollback)  
15. [שימוש בcommit](#שימוש-בcommit)  
16. [שאילתות update ושימוש בcommit](#שאילתות-update-ושימוש-בcommit)  

</div>

### שלב ג':
* [שלב ג'](#שלב-ג)
* * [תרשים DSD של האגף החדש - ניהול נסיעות](#תרשים-dsd-של-האגף-החדש---ניהול-נסיעות)
    * [תרשים erd של האגף החדש](#תרשים-erd-של-האגף-החדש)
    * [תרשים erd משולב](#תרשים-erd-משולב)
    * [תרשים dsd אחרי אינטגרציה](#תרשים-dsd-אחרי-אינטגרציה)
    * [אלגוריתם הינדוס לאחור](#אלגוריתם-הינדוס-לאחור)
* [תהליך אינטגרציית הנתונים](#תהליך-אינטגרציית-הנתונים)
    * [אינטגרציית נהגים ורכבים](#אינטגרציית-נהגים-ורכבים)
    * [אינטגרציית תחזוקה](#אינטגרציית-תחזוקה)
    * [אינטגרציית נסיעות](#אינטגרציית-נסיעות)
* [מבטים](#מבטים)
    * [מבט לניהול נסיעות - View_Operations_Trip_Overview](#מבט-לניהול-נסיעות---view_operations_trip_overview)
    * [תיאור השאילתות (ניהול נסיעות)](#תיאור-השאילתות)
        * [חיפוש נסיעות שהושלמו לפי לקוח](#חיפוש-נסיעות-שהושלמו-לפי-לקוח)
        * [תפוסה לפי רכב](#תפוסה-פי-רכב)
    * [מבט לניהול צי ותחזוקה - View_Fleet_Maintenance_Analytics](#מבט-לניהול-צי-ותחזוקה---view_fleet_maintenance_analytics)
    * [תיאור השאילתות (צי ותחזוקה)](#תיאור-השאילתות-1)
        * [ניתוח עלויות תחזוקה לפי דגם](#ניתוח-עלויות-תחזוקה-לפי-דגם)
        * [רשימת טיפולים פתוחים](#רשימת-טיפולים-פתוחים)

---

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

## אפיון המערכת - מסכי AI Studio:

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


## הסבר על הקשרים המופיעים בתרשימים:
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
* **הסבר:** רכב אחד יכול להיות קשור למספר פוליסות ביטוח לאורך השנים (כמו ביטוח חובה, מקיף, או חידוש פוליסה שנתית). כל רשומה בטבלת הביטוח מתייחסת לרכב אחד בלבד.
* **חובה/רשות:** **חובה** - המערכת דורשת שכל רכב יהיה מבוטח כדי שיוכל לפעול בבטחה.

### 4. מתחזק (Vehicle - MAINTENANCE)
קשר המעקב אחר תקינות כלי הרכב:
* **סוג הקשר:** אחד-לרבים ($1:N$).
* **הסבר:** עבור רכב אחד נרשמים דוחות תחזוקה רבים (כמו טיפול 10,000, החלפת צמיגים, תיקון תקלה). כל דוח תחזוקה משויך לרכב הספציפי שעבר את הטיפול.
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


## הטבלאות:
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
<img width="873" height="624" alt="image" src="https://github.com/user-attachments/assets/3d29a187-b9e0-4b73-8998-c2e78fac7109" />

## שחזור נתונים:
<img width="817" height="449" alt="image" src="https://github.com/user-attachments/assets/639acdf9-1a87-4490-93da-3ed0e29dca38" />

## שלב ב׳:
## שאילתות select:
## שאילתא שמחשבת ממוצע עלות תחזוקה לפי סוג רכב + יצרן + שנה: 
<img width="551" height="221" alt="image" src="https://github.com/user-attachments/assets/d0898c23-1cac-4817-8d34-7945f92aceb3" />
<img width="702" height="166" alt="image" src="https://github.com/user-attachments/assets/a1232ae8-8425-488c-9329-34112cf47b7a" />

## שאילתא שמחזירה את רשימת הרכבים עם ביטוח לא בתוקף: 
<img width="429" height="222" alt="image" src="https://github.com/user-attachments/assets/1f67846c-cec4-417c-ad47-c9ddc966a1c7" />
<img width="297" height="165" alt="image" src="https://github.com/user-attachments/assets/e503995d-093c-4c18-a209-08e4951dde54" />

## שאילתא שמחזירה פילוח כמות טיפולי התחזוקה לפי ימי השבוע, מוצג בסדר יורד מהיום העמוס ביותר:
<img width="592" height="118" alt="image" src="https://github.com/user-attachments/assets/dd40ee74-5ed0-483f-8358-955b93898d71" />
<img width="267" height="171" alt="image" src="https://github.com/user-attachments/assets/41073bbd-7aaf-4900-b9d8-cac1b868d388" />


## שאילתא שמחזירה את רשימת הרכבים שעלות התחזוקה שלהם גבוה מהממוצע הכללי
 <img width="604" height="492" alt="image" src="https://github.com/user-attachments/assets/3f8d7675-23de-4332-ad2e-9116f5f68ea6" />
<img width="649" height="165" alt="image" src="https://github.com/user-attachments/assets/6a1d35e0-71d5-4301-9795-27fecd9fb13e" />

 ## שאילתא שמחזירה רשימה של נהגים שלא ביצעו נסיעה בחודש האחרון - יותר יעילה

<img width="533" height="199" alt="image" src="https://github.com/user-attachments/assets/9d3f749e-13b0-4a5d-826a-f595050417e0" />
<img width="434" height="168" alt="image" src="https://github.com/user-attachments/assets/d90f093d-08b1-457c-97e1-95d10f2c0b17" />

##  שאילתא שמחזירה רשימה של נהגים שלא ביצעו נסיעה בחודש האחרון - פחות יעילה
<img width="521" height="180" alt="image" src="https://github.com/user-attachments/assets/62aed3d7-d19f-4eb4-a1d8-b4037e08efff" />
<img width="436" height="128" alt="image" src="https://github.com/user-attachments/assets/1d46250c-7415-4490-b965-0ba6ff4b662c" />

### השוואת יעילות בין שתי שאילתות למציאת נהגים שלא ביצעו נסיעה בחודש האחרון

שתי השאילתות מחזירות את רשימת הנהגים שלא ביצעו נסיעות במהלך החודש האחרון, אך הן ממומשות בדרכים שונות.

השאילתא הראשונה משתמשת ב־`NOT EXISTS`, ולכן היא נחשבת יעילה יותר. עבור כל נהג בטבלת `Driver`, מתבצעת בדיקה האם קיימת לפחות נסיעה אחת בטבלת `Trip` במהלך החודש האחרון. ברגע שנמצאת התאמה, בסיס הנתונים יכול לעצור את הבדיקה עבור אותו נהג ולהמשיך הלאה. בנוסף, השימוש ב־`SELECT 1` בתוך תת־השאילתה מצביע על כך שמעניין אותנו רק קיום רשומה, ולא תוכן העמודות.

לעומת זאת, השאילתא השנייה משתמשת ב־`NOT IN` יחד עם תת־שאילתה שמחזירה את כל הנהגים שביצעו נסיעה בחודש האחרון. תת־השאילתה כוללת `DISTINCT`, פעולה שמוסיפה עלות חישובית כאשר קיימות כפילויות רבות בטבלת `Trip`. לאחר יצירת הרשימה, מתבצעת השוואה מול כל הנהגים בטבלת `Driver`.

בנוסף, `NOT IN` עלול להיות רגיש לערכי `NULL`, דבר שעלול לגרום לתוצאות שגויות או בלתי צפויות. לעומת זאת, `NOT EXISTS` נחשב בטוח יותר בהיבט זה.

לכן, השאילתא הראשונה עדיפה מבחינת יעילות, קריאות, והתנהגות נכונה במצבים שונים של נתונים.

## שאילתא שמחזירה את הרכבים שזמינים השבוע (לא משוריינים לנסיעות) - יעילה
<img width="531" height="246" alt="image" src="https://github.com/user-attachments/assets/ed4a9580-1a53-4e28-8840-02d5777696eb" />
<img width="365" height="166" alt="image" src="https://github.com/user-attachments/assets/eb106da5-f137-4b6b-9a5d-e28b6264151f" />

## שאילתא שמחזירה את הרכבים שזמינים השבוע (לא משוריינים לנסיעות) - פחות יעילה
<img width="683" height="242" alt="image" src="https://github.com/user-attachments/assets/fd1e8083-0057-40b7-a002-929d0ce5db86" />
<img width="361" height="163" alt="image" src="https://github.com/user-attachments/assets/7bf063e0-db67-4e42-a80f-57327fce1b2f" />

## השוואת יעילות בין שתי שאילתות למציאת רכבים זמינים השבוע -

שתי השאילתות מחזירות רכבים שאינם משוריינים לנסיעות במהלך השבוע הקרוב.

השאילתא הראשונה משתמשת ב־`NOT EXISTS`, ולכן היא נחשבת יעילה ובטוחה יותר. עבור כל רכב, בסיס הנתונים בודק האם קיימת נסיעה מתאימה בטבלת `Trip` בשבוע הקרוב. ברגע שנמצאת נסיעה אחת עבור אותו רכב, אין צורך להמשיך לבדוק נסיעות נוספות עבורו, ולכן ניתן לעצור את החיפוש מוקדם.

לעומת זאת, השאילתא השנייה משתמשת ב־`NOT IN` יחד עם תת־שאילתה שמחזירה את כל הרכבים שכבר משוריינים השבוע. בנוסף, נעשה שימוש ב־`DISTINCT` כדי להסיר כפילויות של `VehicleID`, פעולה שעלולה להיות יקרה יותר כאשר טבלת `Trip` גדולה. לאחר יצירת הרשימה, בסיס הנתונים צריך להשוות את כל רכבי `Vehicle` מול הרשימה שנוצרה.

בנוסף, `NOT IN` רגיש לערכי `NULL`. אם תת־השאילתה מחזירה `NULL`, התוצאה עלולה להיות שגויה או ריקה, ולכן נדרש להוסיף תנאי כמו `VehicleID IS NOT NULL`. לעומת זאת, `NOT EXISTS` אינו סובל מבעיה זו באותה צורה.

לכן, השאילתא עם `NOT EXISTS` עדיפה מבחינת יעילות, קריאות ובטיחות לוגית.

## שאילתא המחשבת עלות ביטוח ממוצע לאוטובוסים לפי חברה בסדר יורד - יעילה 
<img width="463" height="163" alt="image" src="https://github.com/user-attachments/assets/1d7978d6-09ff-4f57-8752-a0449173f7f6" />
<img width="326" height="138" alt="image" src="https://github.com/user-attachments/assets/270d04e3-011c-44c6-901a-97d2a4b4df3c" />

## שאילתא המחשבת עלות ביטוח ממוצע לאוטובוסים לפי חברה בסדר יורד - פחות יעילה
<img width="467" height="225" alt="image" src="https://github.com/user-attachments/assets/4e223fb0-963c-4036-811d-0478eb9e1800" />
<img width="314" height="137" alt="image" src="https://github.com/user-attachments/assets/da41271a-0290-4f1c-b0bc-6de22b6fd325" />

### השוואת יעילות בין שתי שאילתות לחישוב עלות ביטוח ממוצעת לאוטובוסים לפי חברה

שתי השאילתות מחשבות את עלות הביטוח הממוצעת עבור אוטובוסים (`VehicleType = 'Bus'`) לפי חברת ביטוח, וממיינות את התוצאות בסדר יורד. ההבדל ביניהן הוא באופן הסינון והחיבור בין הטבלאות `Insurance` ו־`Vehicle`.

השאילתא הראשונה משתמשת ב־`JOIN` בין הטבלאות, ולכן נחשבת יעילה וברורה יותר. בסיס הנתונים מחבר ישירות בין `Insurance` ל־`Vehicle` לפי `VehicleID`, ולאחר מכן מסנן רק רכבים מסוג אוטובוס. גישה זו מאפשרת לאופטימייזר של מסד הנתונים לבחור תכנית ביצוע יעילה (כגון שימוש באינדקסים על `VehicleID`), ומונעת יצירת מבני ביניים מיותרים.

לעומת זאת, השאילתא השנייה משתמשת בתת־שאילתה עם `IN`, שבה תחילה נשלפת רשימת כל ה־`VehicleID` של אוטובוסים מטבלת `Vehicle`, ולאחר מכן מתבצעת השוואה מול טבלת `Insurance`. גישה זו פחות ישירה, ועלולה להיות פחות יעילה כאשר מדובר בכמות גדולה של נתונים, משום שנדרשת בנייה של רשימת ערכים והשוואה אליה.

בנוסף, השימוש ב־`JOIN` משקף בצורה טבעית יותר את הקשר בין הטבלאות (מפתח זר), ולכן נחשב קריא ונכון יותר מבחינה תכנונית.

לסיכום, השאילתא המבוססת על `JOIN` עדיפה מבחינת ביצועים, קריאות, והתאמה למבנה היחסים בין הטבלאות.

## שאילתא המחשבת מי הם חמשת הנהגים שביצעו הכי הרבה נסיעות בשנה האחרונה - יעילה

<img width="695" height="228" alt="image" src="https://github.com/user-attachments/assets/e8b7843b-f5ce-4705-8589-cd110383ec47" />
<img width="523" height="168" alt="image" src="https://github.com/user-attachments/assets/c828d1e4-d73d-4d43-9af3-42b450fc86e7" />

## שאילתא המחשבת מי הם חמשת הנהגים שביצעו הכי הרבה נסיעות בשנה האחרונה - פחות יעילה
<img width="557" height="257" alt="image" src="https://github.com/user-attachments/assets/a38d3c42-89d2-4870-bf3b-0af02e7282d6" />
<img width="523" height="166" alt="image" src="https://github.com/user-attachments/assets/f5443153-30b7-46b3-950b-613632a3008a" />

### השוואת יעילות בין שתי שאילתות למציאת חמשת הנהגים שביצעו הכי הרבה נסיעות בשנה האחרונה

שתי השאילתות מחזירות את חמשת הנהגים שביצעו את מספר הנסיעות הגבוה ביותר במהלך השנה האחרונה, אך הן ממומשות בגישות שונות.

השאילתא הראשונה משתמשת ב־`JOIN` בין הטבלאות `Driver` ו־`Trip`, יחד עם `GROUP BY` ואגרגציה (`COUNT`). בסיס הנתונים מסנן תחילה את הנסיעות הרלוונטיות (השנה האחרונה), ולאחר מכן מבצע חישוב מרוכז של מספר הנסיעות לכל נהג בקבוצה אחת. גישה זו יעילה משום שכל טבלת `Trip` נסרקת פעם אחת בלבד, והחישוב מתבצע בצורה קבוצתית.

לעומת זאת, השאילתא השנייה משתמשת בתת־שאילתה קורלטיבית (correlated subquery) בתוך ה־`SELECT`. עבור כל נהג בטבלת `Driver`, מתבצעת שאילתה נוספת לטבלת `Trip` שמחשבת את מספר הנסיעות שלו בשנה האחרונה. כלומר, אם יש N נהגים, תת־השאילתה תתבצע N פעמים — דבר שעלול להיות יקר מאוד כאשר מספר הנהגים גדול.

בנוסף, בשאילתא השנייה מתבצע חישוב גם עבור נהגים שלא ביצעו כלל נסיעות, מה שמוסיף עבודה מיותרת, בעוד שבשאילתא הראשונה רק נהגים עם נסיעות רלוונטיות נכנסים לחישוב.

לכן, השאילתא הראשונה עדיפה מבחינת יעילות, שכן היא מבצעת אגרגציה אחת על הנתונים, בעוד שהשאילתא השנייה מבצעת חישוב חוזר עבור כל נהג בנפרד.


## אילוצים
## אילוצים בטבלת רכב -
האילוץ מוודא כי ניתן להזין לטבלת הרכבים רק רכבים עם קיבולת חיובית:
<img width="390" height="61" alt="image" src="https://github.com/user-attachments/assets/42944a71-480c-4b9a-9714-a531bd04b041" />
<img width="751" height="45" alt="image" src="https://github.com/user-attachments/assets/cbae73d6-33d6-4232-8b51-92402f47d042" />
<img width="729" height="88" alt="image" src="https://github.com/user-attachments/assets/ff144aa5-fb26-4602-9897-c3d576b94832" />

האילוץ מוודא כי ניתן להזין לטבלת הרכבים רק רכבים מתוך הרשימה שהוגדרה:

<img width="488" height="63" alt="image" src="https://github.com/user-attachments/assets/5a8ae45c-39ab-4906-b19f-0b33d39b8cf7" />
<img width="747" height="45" alt="image" src="https://github.com/user-attachments/assets/9688fb6d-701f-41b0-bb48-5fb1447bc9bf" />
<img width="629" height="51" alt="image" src="https://github.com/user-attachments/assets/3480a6fc-6cac-497b-97b8-60d21fbd503c" />


## אילוצים בטבלת נהג -
האילוץ מוודא כי ניתן להזין לטבלת הנהגים רק סוגי רישיון חוקיים מתוך הרשימה שהוגדרה:

<img width="367" height="64" alt="image" src="https://github.com/user-attachments/assets/74a05fe5-edcf-4eea-b37c-558949be1b01" />
<img width="808" height="49" alt="image" src="https://github.com/user-attachments/assets/6458a4f5-aa75-496d-b92e-0b81e5874830" />
<img width="671" height="49" alt="image" src="https://github.com/user-attachments/assets/6dc549dc-e6c3-426f-91f7-0aef190a9da3" />

האילוץ מוודא כי ניתן להזין לטבלת הנהגים רק טלפון שמתחיל בספרות 05 והוא בעל 10 ספרות:

<img width="408" height="65" alt="image" src="https://github.com/user-attachments/assets/62d3297b-425c-4092-8727-c744e9f0b6e0" />
<img width="807" height="49" alt="image" src="https://github.com/user-attachments/assets/01b77f31-b320-4748-bf11-75b66af9cab0" />
<img width="673" height="48" alt="image" src="https://github.com/user-attachments/assets/cc71f977-a55d-4621-a405-7d50ba98c7e9" />

האילוץ מוודא כי ניתן להזין לטבלת הנהגים רק תאריך גיוס שהוא עד היום:
<img width="304" height="68" alt="image" src="https://github.com/user-attachments/assets/f2ed5d05-a923-49ab-afc8-b5d76850f8e2" />
<img width="815" height="46" alt="image" src="https://github.com/user-attachments/assets/dd96420c-46e2-42bd-99cd-385b0e1a7960" />
<img width="649" height="46" alt="image" src="https://github.com/user-attachments/assets/c1057062-fef9-40f4-baaf-66fd15c9826b" />

## אילוצים בטבלת נסיעה -
האילוץ מוודא כי ניתן להזין לטבלת הנסיעה רק מחיר חיובי:
<img width="366" height="61" alt="image" src="https://github.com/user-attachments/assets/34ead6a8-d129-4fb8-8e96-7e4ebdf24594" />
<img width="1206" height="55" alt="image" src="https://github.com/user-attachments/assets/5a21ef71-c4e2-436a-be9a-2c60e1a70b95" />
<img width="727" height="52" alt="image" src="https://github.com/user-attachments/assets/8d832248-2be9-4c0d-a76e-0ffb30e6e5df" />

האילוץ מוודא כי ניתן להזין לטבלת הנסיעה רק מס׳ נוסעים חיובי:
<img width="372" height="67" alt="image" src="https://github.com/user-attachments/assets/0e02f4ea-f71d-467a-8d58-b2bf11caab09" />
<img width="1199" height="53" alt="image" src="https://github.com/user-attachments/assets/bd8bfd72-ced2-4434-aa83-01e91c71e48f" />
<img width="730" height="40" alt="image" src="https://github.com/user-attachments/assets/70ce9a61-bc5b-4e36-817b-932a48c666a0" />

האילוץ מוודא כי ניתן להזין לטבלת הנסיעה רק מס׳ שעות חיובי:
<img width="371" height="71" alt="image" src="https://github.com/user-attachments/assets/a9ce0a72-3fab-42c0-9f1b-7da1882e09b2" />
<img width="1192" height="50" alt="image" src="https://github.com/user-attachments/assets/bf5ce1cb-ad17-4806-bfb2-f724331bcd13" />
<img width="735" height="43" alt="image" src="https://github.com/user-attachments/assets/c58da20f-b107-4d21-bd49-b2c3dae49e1d" />

האילוץ מוודא כי ניתן להזין לטבלת הנסיעה רק סטטוס מהרשימה שהוגדרה:
<img width="613" height="67" alt="image" src="https://github.com/user-attachments/assets/6df71b81-6e53-4922-b2aa-ed38a652a2d7" />
<img width="1192" height="49" alt="image" src="https://github.com/user-attachments/assets/534d63f5-fd91-432d-85dc-0269c50c3709" />
<img width="733" height="51" alt="image" src="https://github.com/user-attachments/assets/f27d7945-72b3-4580-8251-1daaab89f416" />



## אילוצים בטבלת תדלוק -
האילוץ מוודא כי ניתן להזין לטבלת התדלוק רק כמות דלק חיובית:
<img width="358" height="70" alt="image" src="https://github.com/user-attachments/assets/a0d33d9f-529f-45ad-aed5-754f6dbb4cac" />
<img width="846" height="43" alt="image" src="https://github.com/user-attachments/assets/c151b01e-d16c-4b8a-b2e7-0fa6e354c06e" />
<img width="696" height="54" alt="image" src="https://github.com/user-attachments/assets/f5c72437-9a7f-492c-afc8-708887f8d21e" />

האילוץ מוודא כי ניתן להזין לטבלת התדלוק רק מחיר לדלק חיובי:
<img width="322" height="63" alt="image" src="https://github.com/user-attachments/assets/7d96c0cc-0418-4bf1-adc5-b7be315b6fe9" />
<img width="861" height="47" alt="image" src="https://github.com/user-attachments/assets/4c695732-3d0a-46b1-a164-e29a8a42f8f5" />
<img width="673" height="55" alt="image" src="https://github.com/user-attachments/assets/aaf266e7-cc39-417e-80a3-4c67ebbef7cb" />

## אילוצים בטבלת תחזוקה -
האילוץ מוודא כי ניתן להזין לטבלת התחזוקה רק סטטוס מהרשימה שהוגדרה:
<img width="740" height="87" alt="image" src="https://github.com/user-attachments/assets/caf442e8-0fec-4505-9baf-178e8e5c504f" />
<img width="993" height="45" alt="image" src="https://github.com/user-attachments/assets/738532a7-0278-4d77-ba82-8692a7972d1f" />
<img width="804" height="43" alt="image" src="https://github.com/user-attachments/assets/30d556e8-51be-464b-b8ef-f75bc56d0097" />

האילוץ מוודא כי ניתן להזין לטבלת התחזוקה רק מחיר חיובי או שווה ל0:
<img width="419" height="62" alt="image" src="https://github.com/user-attachments/assets/fcf1062a-8c07-4356-aaeb-f7fcc4cae878" />
<img width="998" height="52" alt="image" src="https://github.com/user-attachments/assets/ee64fcd6-7672-4123-b17a-f76408646de4" />
<img width="783" height="39" alt="image" src="https://github.com/user-attachments/assets/9649dbe5-9db5-4a6f-ae98-460692519d0c" />

האילוץ מוודא כי ניתן להזין לטבלת התחזוקה רק סוג טיפול מהרשימה שהוגדרה:
<img width="990" height="67" alt="image" src="https://github.com/user-attachments/assets/ee0e54a1-2730-4652-88e2-84eaa67724a8" />
<img width="999" height="57" alt="image" src="https://github.com/user-attachments/assets/b3fab8ef-42c2-4854-90a8-6cbc1fa9f6aa" />
<img width="693" height="46" alt="image" src="https://github.com/user-attachments/assets/0432402e-940f-4bb6-adc7-b8ae0c869e7e" />


## אילוצים בטבלת ביטוח -
האילוץ מוודא כי ניתן להזין לטבלת הביטוח רק תאריך סיום ביטוח שמאוחר יותר מתאריך תחילת ביטוח:
<img width="301" height="65" alt="image" src="https://github.com/user-attachments/assets/10d82c50-d507-4c78-80ee-6b90efaa01a7" />
<img width="886" height="52" alt="image" src="https://github.com/user-attachments/assets/037ac582-2d09-4931-941b-c41f3f0bf81f" />
<img width="673" height="53" alt="image" src="https://github.com/user-attachments/assets/ce6e1760-d736-4068-948c-486f1c51a717" />

האילוץ מוודא כי ניתן להזין לטבלת הביטוח רק מחיר חיובי:
<img width="374" height="68" alt="image" src="https://github.com/user-attachments/assets/ed7e4c97-44f6-48b4-8b62-140a02a3641e" />
<img width="903" height="46" alt="image" src="https://github.com/user-attachments/assets/2b95c7fe-e510-480c-a80a-8b919eecab5e" />
<img width="721" height="48" alt="image" src="https://github.com/user-attachments/assets/14b2a0e6-0f33-4987-a18c-c2923761a034" />

## שאילתות delete ושימוש בrollback -
מחיקת אוטובסים משנת ייצור נמוכה מ-2019 שאינן משובצות לנסיעות עתידיות וכל הפרטים המשוייכים אליהן
<img width="772" height="459" alt="image" src="https://github.com/user-attachments/assets/40935698-26e3-41f4-bf17-81b1e84736d1" />
טבלת רכב לאחר ההרצה -
<img width="109" height="67" alt="image" src="https://github.com/user-attachments/assets/f4c2e764-535c-4451-9a52-a907e45d417d" />
החזרת בסיס הנתונים לקדמותו -
<img width="117" height="76" alt="image" src="https://github.com/user-attachments/assets/181c49ea-e29f-4ec3-9a46-a07773cd54a9" />

מחיקת תדלוקים מעל שנה לרכבים שלא עברו טיפול צמיגים
<img width="743" height="283" alt="image" src="https://github.com/user-attachments/assets/39ae6b47-870a-4f7f-9439-322c262972db" />
טבלת תדלוק לאחר הרצה -
<img width="113" height="74" alt="image" src="https://github.com/user-attachments/assets/87fec102-d8b4-49fe-a591-49d072d19eda" />

החזרת בסיס הנתונים לקדמותו -
<img width="112" height="70" alt="image" src="https://github.com/user-attachments/assets/763ae28c-4c55-4c76-98f0-10cd772ae0a4" />

מחיקת נסיעות שמתנגשות עם לו״ז תחזוקה -
<img width="571" height="184" alt="image" src="https://github.com/user-attachments/assets/919ed060-19e7-47c9-94d0-9707853958a5" />
טבלת נסיעות לאחר הרצה -
<img width="117" height="68" alt="image" src="https://github.com/user-attachments/assets/e783d273-fa59-49af-a5e3-286235d00610" />

החזרת בסיס הנתונים לקדמותו -
<img width="108" height="71" alt="image" src="https://github.com/user-attachments/assets/bd66b66c-2755-482a-bbe4-d6f3de73a28a" />

## שימוש בcommit -
עדכון עמודת סטטוס בנסיעה ל״הושלם״ או ב״תהליך״ -
<img width="385" height="244" alt="image" src="https://github.com/user-attachments/assets/4c7d66f6-6ece-456f-bba1-c02da9649ed0" />
בדיקה לפני הרצה -
<img width="280" height="24" alt="image" src="https://github.com/user-attachments/assets/deafb3f7-5570-4e16-870d-b068c3740a7a" />
<img width="517" height="400" alt="image" src="https://github.com/user-attachments/assets/888872cf-2db4-46ce-857e-969f63df3fb5" />
בדיקה לאחר הרצה ולפני commit -

<img width="297" height="168" alt="image" src="https://github.com/user-attachments/assets/b81d30e8-45a0-47fb-8345-9528cb26c647" />
בדיקה לאחר commit -
<img width="297" height="168" alt="image" src="https://github.com/user-attachments/assets/8d3e1626-538b-441c-92c1-fa32ac73bafc" />


## שאילתות update ושימוש בcommit -
עדכון סטטוס תחזוקה ״בתהליך״ לטיפולים שהתאריך שלהם הוא מה-30 ימים האחרונים ועד היום:
<img width="736" height="273" alt="image" src="https://github.com/user-attachments/assets/26c53a8c-c5e6-45f6-9736-f6fa94e9fb9a" />

הכנסת נתונים לעמודת עיר בטבלת נהגים:
<img width="1310" height="241" alt="image" src="https://github.com/user-attachments/assets/bac5e72d-4096-4374-9a81-cc4bd79df2d5" />

שידוך בין ביטוח לרכב על מנת להבטיח שלכל רכב יהיה ביטוח אחד בלבד:
<img width="744" height="434" alt="image" src="https://github.com/user-attachments/assets/00660380-51b5-468a-a8ea-eccc4e180d2f" />

עדכון מחיר נסיעה לפי סוג רכב -
<img width="859" height="401" alt="image" src="https://github.com/user-attachments/assets/d68d9f41-3005-472a-bed4-b5cda968b8af" />


## שלב ג':
## תרשים DSD של האגף החדש - ניהול נסיעות:
<img width="1144" height="444" alt="image" src="https://github.com/user-attachments/assets/e888d2d3-b4e3-4e07-b5c3-50b837e5fba3" />

## תרשים erd של האגף החדש:
<img width="1305" height="567" alt="image" src="https://github.com/user-attachments/assets/05932258-cac1-4457-85bb-329c54aadbea" />

## תרשים erd משולב:
<img width="1359" height="519" alt="image" src="https://github.com/user-attachments/assets/2b28311d-8b43-4d91-8f9e-4d6502982390" />

## תרשים dsd אחרי אינטגרציה:
<img width="1236" height="502" alt="image" src="https://github.com/user-attachments/assets/7765207b-4ce3-47c2-90b2-458ce877bf1a" />

## אלגוריתם הינדוס לאחור:
שלב א': מיפוי טבלאות הגיבוי שקיבלנו (זיהוי ישויות).

שלב ב': זיהוי מפתחות זרים (FK) בטבלאות הגיבוי כדי להבין את הקשרים (למשל: איזה נהג קשור לאיזה רכב).

שלב ג': שרטוט הקשרים ב-ERDPlus (יצירת הישויות והקשרים ב"הינדוס לאחור").

שלב ד': השוואה בין ה-ERD שיצרנו לבין ה-ERD המקורי שלנו כדי למצוא נקודות חיבור (ישויות משותפות).


החלטות שהתקבלו בשלב האינטגרציה
בשלב זה ביצענו אינטגרציה מלאה בין בסיס הנתונים שלנו לבין בסיס הנתונים של האגף הנוסף שקיבלנו. מטרתנו המרכזית הייתה ליצור מערכת מאוחדת המאפשרת ניהול צי אופטימלי, תוך מניעת כפילויות, הבטחת תקינות נתונים ויצירת מבנה המשלב את היכולות של שני האגפים.

ההחלטה התכנונית הראשונה שלנו הייתה לאחד ישויות בעלות משמעות עסקית זהה. זיהינו כי שתי המערכות מנהלות רשימות נהגים ורכבים, לכן החלטנו על תהליך של מיזוג נתונים. במקום להחזיק טבלאות נפרדות, יצרנו טבלאות מאוחדות עבור הנהגים והרכבים, כאשר ביצענו מיפוי מדויק למזהים (IDs) כדי להבטיח מפתח ראשי ייחודי לכל רשומה במערכת החדשה. כמו כן, איחדנו את טבלאות הנסיעות. בחרנו לשמר את המבנה של הנסיעות שלנו (Trip) והטמענו בו שדות רלוונטיים מתוך ישות הנסיעות (Ride) של האגף השני, כגון תאריך ההזמנה, כדי להעשיר את המידע העסקי.

בנוסף, הטמענו את הישויות החדשות שהגיעו מהאגף השני – לקוחות ומסלולים (Route) – בתוך הסכמה שלנו. החלטנו לשמר ישויות אלו כחלק בלתי נפרד מהמערכת המשולבת, כיוון שהן מאפשרות ניהול רחב יותר של הקשר מול הלקוח ומעקב אחר נתיבי הנסיעה. לצד זאת, החלטנו לשמר את הישויות הייחודיות שהיו קיימות רק במערכת שלנו, כגון תדלוקים (FuelLog) וביטוחים (Insurance). אלו נותרו במערכת המשולבת ומקושרות לרכבים המאוחדים, כיוון שהן חיוניות לניתוח עלויות ותחזוקה שוטפת של הצי.

תהליך ההינדוס לאחור (Reverse Engineering) שביצענו התבסס על אלגוריתם עבודה סדור. תחילה מיפינו את כל טבלאות הגיבוי שקיבלנו וזיהינו את כל המפתחות הראשיים והזרים (PK/FK) כדי להבין את מבנה הקשרים המקורי. לאחר מכן, בנינו מחדש את תרשים ה-DSD לפי הקשרים שמצאנו בטבלאות. בשלב הבא, שרטטנו את הישויות החדשות ב-ERDPlus והגדרנו את נקודות החיבור לישויות הקיימות שלנו. לבסוף, ביצענו ולידציה כדי לוודא שה-ERD המאוחד תומך בכלל הכללים העסקיים של שני האגפים יחד.

לסיום, בהתאם להנחיות, לא יצרנו את הטבלאות מחדש, אלא השתמשנו בפקודות SQL של שינוי מבנה (כמו ALTER TABLE) כדי להוסיף עמודות חסרות או לבצע התאמות, ופקודות INSERT כדי להעביר את הנתונים מהגיבוי של האגף השני לתוך המבנה של המערכת המקורית שלנו. תהליך זה הבטיח שהנתונים מהאגף שקיבלנו השתלבו באופן תקין במבנה הקיים מבלי לפגוע ברצף העבודה של המערכת שלנו.

תהליך שינוי שמות טבלאות  <img width="605" height="229" alt="image" src="https://github.com/user-attachments/assets/172b55d7-fc49-4696-ad2e-a70fd160c9eb" />

בשלב ראשוני זה של אינטגרציית הנתונים, נדרשנו לבצע סטנדרטיזציה של שמות הטבלאות בבסיס הנתונים המשולב. מכיוון שבמהלך המיזוג עלו התנגשויות בשמות בין המערכת שלנו למערכת שקיבלנו, החלטנו על שינוי מבני מקיף באמצעות פקודות ALTER TABLE.

התהליך כלל הרצה של פקודות RENAME TO, אשר שינו את שמות הטבלאות המקוריות – vehicle, driver, ו-maintenance – לשמות חדשים: vehicle1, driver1, ו-maintenance1. פעולה זו בוצעה כדי להבטיח אחידות בממשק העבודה החדש, לאפשר עבודה מול הטבלאות המאוחדות ללא בלבול מול טבלאות הגיבוי המקוריות, ולהכין את התשתית להטמעת נתונים נוספים לתוך מבנה הטבלאות המעודכן, מבלי לפגוע ביחסים הלוגיים הקיימים בין הישויות השונות בבסיס הנתונים.

הרחבת הסכמה לישויות חדשות <img width="481" height="412" alt="image" src="https://github.com/user-attachments/assets/164d49a5-5f05-488d-a6c2-c7f9b3fb5f45" />

כחלק מתהליך האינטגרציה והטמעת היכולות של האגף החדש במערכת המאוחדת, ביצענו הרחבה של סכמת בסיס הנתונים באמצעות יצירת שתי טבלאות חדשות: customer ו-route.

טבלת ה-customer הוקמה כדי לאפשר ניהול מרכזי ומסודר של לקוחות הארגון. הגדרנו את שדה ה-id כמפתח ראשי (Primary Key) כדי להבטיח זיהוי חד-ערכי לכל לקוח, לצד עמודות המאחסנות פרטים מזהים כגון שם מלא, כתובת אימייל ומספר טלפון, מה שמאפשר תמיכה טובה יותר בשירות הלקוחות של המערכת המשולבת.

במקביל, יצרנו את טבלת ה-route, המיועדת לניהול נתיבי נסיעה ומיקומים. בטבלה זו בחרנו ליישם מפתח ראשי מורכב (Composite Primary Key) המורכב מהשדות origin (מוצא) ו-destination (יעד). בחירה זו מאפשרת לנו להגדיר בצורה ייחודית כל מסלול נסיעה קיים. בנוסף, כללנו שדות כגון מרחק (distancekm) וזמן נסיעה משוער (estimatedtraveltime), הנתונים הללו משמשים כתשתית תכנונית המאפשרת לאופטימיזציה של תכנון הנסיעות במערכת המאוחדת. הטמעת טבלאות אלו מבטיחה שכל המידע התפעולי שהגיע מהאגף החדש יישמר בצורה מסודרת ויהיה נגיש לביצוע שאילתות ודוחות במערכת הסופית.


הרחבת מבנה הטבלאות<img width="634" height="296" alt="image" src="https://github.com/user-attachments/assets/1bab0c27-7331-4862-9c1c-7523cbb32027" />

לצורך תמיכה בנתונים שהגיעו מהאגף הנוסף, הרחבנו את מבנה הטבלאות הקיים באמצעות פקודות ALTER TABLE בשילוב ADD COLUMN IF NOT EXISTS.

בטבלת ה-vehicle1, הוספנו עמודות ייעודיות לניהול מאפייני הצי: model (דגם), carcolor (צבע) ו-capacity (קיבולת). הרחבה זו מאפשרת לנו לאחסן את נתוני הרכבים שהגיעו מהמערכת החדשה בתוך הטבלה הקיימת שלנו, ללא צורך ביצירת טבלאות נוספות.

בטבלת ה-trip, ביצענו הרחבה תפעולית על ידי הוספת עמודות customer_id (לקישור ללקוח) וזוג עמודות route_origin ו-route_destination (לציון מסלול הנסיעה). הוספת שדות אלו יוצרת קשרים לוגיים (Foreign Keys) מול טבלאות הלקוחות והמסלולים שהקמנו, ומאפשרת לשייך כל נסיעה במערכת המאוחדת ללקוח רלוונטי ולנתיב נסיעה מוגדר.


הגדרת אילוצי שלמות נתונים<img width="1147" height="94" alt="image" src="https://github.com/user-attachments/assets/587728c2-1ac5-455e-a40b-e5a3a3380025" />

כדי להבטיח את שלמות הנתונים (Data Integrity) במערכת המאוחדת, הגדרנו מפתחות זרים (Foreign Keys) על טבלת ה-trip.

באמצעות פקודות ALTER TABLE ו-ADD CONSTRAINT, יצרנו קשרים מחייבים בין הנסיעות לבין הטבלאות החדשות: האילוץ fk_trip_customer מקשר בין customer_id בנסיעה לבין הלקוח בטבלת ה-customer, והאילוץ fk_trip_route מחייב שכל מסלול בנסיעה יהיה קיים בטבלת ה-route. הגדרות אלו מונעות הזנת נתונים שגויים (כגון נסיעה ללא לקוח או במסלול שלא קיים) ומבטיחות שכל קשרי הגומלין בין הישויות נשמרים באופן עקבי בכל המערכת.

## תהליך אינטגרציית הנתונים: 
## אינטגרציית נהגים ורכבים:
בשלב הראשון הוספנו עמודת status לטבלת ה-driver1 לניהול אחיד של מצב הנהג. העברת הנתונים בוצעה דרך טבלאות עזר זמניות (temp_driver_import, temp_vehicle_import), שאפשרו ביצוע פעולות טיוב בטוחות לפני המיזוג הסופי:

נהגים: בצענו סטנדרטיזציה למספרי טלפון באמצעות SUBSTRING ושרשור קידומת '05'. הנתונים הועברו לטבלה הראשית תוך הקצאת מזהים (driverid) עוקבים בעזרת ROW_NUMBER ו-COALESCE, ושימוש ב-split_part לפיצול שמות. חוסרים בנתונים (כמו סוג רישיון או עיר) הושלמו באמצעות הגרלה אקראית (random) כדי לעמוד באילוצי הסכמה.

רכבים: ניקינו את מספרי הרישוי באמצעות regexp_replace והשתמשנו ב-split_part לחילוץ היצרן מהדגם. בדומה לנהגים, השלמנו ערכים חסרים (דגם וצבע) כדי להבטיח שלמות נתונים.

ניקוי סופי: לאחר ה-INSERT, ביצענו UPDATE ממוקד לתיקון ערכים ריקים בסטטוסים וסטנדרטיזציה נוספת למספרי הטלפון ב-driver1 באמצעות LPAD, וסיימנו ב-DROP TABLE למחיקת טבלאות העזר.

## אינטגרציית תחזוקה:
הטמענו את היסטוריית הטיפולים ל-maintenance1 תוך שימוש ב-JOIN מול טבלת ה-vehicle1. הקישור הלוגי התבסס על התאמת מספר הרישוי המנוקה מהנתונים הגולמיים למזהה הרכב (vehicleid) במערכת המאוחדת. הקצאנו מזהי תחזוקה ייחודיים וקבענו סטטוס ברירת מחדל של 'Completed' לכל הרשומות המיובאות, מה שהבטיח תאימות מלאה לצי המאוחד.

## אינטגרציית נסיעות:
הטמעת הנסיעות בוצעה בטבלת ה-trip לאחר עדכון ה-CHECK CONSTRAINT כדי לאפשר סטטוס 'Pending'.

תהליך המיזוג: השתמשנו ב-INNER JOIN כפול מול טבלאות הנהגים והרכבים כדי לוודא שכל נסיעה מקושרת לישות קיימת בלבד.

מניעת כפילויות וטיוב: הוספנו פילטר WHERE NOT EXISTS כדי למנוע כפילויות הזמנה. ביצענו המרות סוגים (timestamp, integer) ושימוש ב-COALESCE לניהול ערכים ריקים, תוך קיצור מחרוזות (פונקציית LEFT) כדי להתאים את הנתונים למגבלות האורך של העמודות.

## מבטים:
## מבט לניהול נסיעות - View_Operations_Trip_Overview:
מבט זה משמש כמרכז בקרה תפעולי. הוא מבצע JOIN בין הנסיעות (trip), הלקוחות (customer) והרכבים (vehicle1) כדי להציג בטבלה אחת את כל המידע הרלוונטי לכל נסיעה – מהלקוח ועד לרכב המשובץ. הוא הופך את המידע המבוזר בטבלאות שונות לדו"ח קריא וברור עבור מנהלי התפעול
SELECT * FROM View_Operations_Trip_Overview LIMIT 10;

<img width="1256" height="366" alt="image" src="https://github.com/user-attachments/assets/aa03f21e-b4d8-482e-a44e-af781b68493c" />

## תיאור השאילתות:
## חיפוש נסיעות שהושלמו לפי לקוח:
שאילתא זו מסננת את המבט כדי לשלוף היסטוריית נסיעות של לקוח ספציפי (בדוגמה: Stoddard Abbate) שסטטוס הנסיעה שלהן הוא 'Completed', מה שמאפשר מעקב אישי אחר שירות הלקוח.
SELECT * FROM View_Operations_Trip_Overview WHERE customer_name = 'Stoddard Abbate' AND trip_status = 'Completed';
<img width="1306" height="699" alt="image" src="https://github.com/user-attachments/assets/4f5862ed-f9bc-4c84-ad81-cd957dabfe83" />

SELECT vehicle_model, COUNT(tripid) AS total_trips FROM View_Operations_Trip_Overview GROUP BY vehicle_model;
## תפוסה לפי רכב:
שאילתה זו מבצעת אגרגציה (GROUP BY) לפי דגם הרכב וסופרת את כמות הנסיעות הכוללת לכל דגם, מה שעוזר להבין אילו דגמים בצי הם הפעילים ביותר.
<img width="436" height="530" alt="image" src="https://github.com/user-attachments/assets/c1e6708a-24f7-487c-a3d8-5efb80668e96" />

## מבט לניהול צי ותחזוקה - View_Fleet_Maintenance_Analytics:
מבט זה מקשר בין הרכבים (vehicle1) לבין היסטוריית התחזוקה (maintenance1) ונתוני הנסיעות (trip). הוא מספק מדדים תפעוליים לכל רכב, כגון עלויות תחזוקה, תאריכי טיפולים וספירת נסיעות שבוצעו, ומאפשר ניתוח ביצועים מקיף של כל כלי רכב בצי.
SELECT * FROM View_Fleet_Maintenance_Analytics LIMIT 10;
<img width="1041" height="579" alt="image" src="https://github.com/user-attachments/assets/bdb230a9-8d2a-4cc8-8d54-561adc3a41a3" />

## תיאור השאילתות:
## ניתוח עלויות תחזוקה לפי דגם:
שאילתה זו מסכמת את כמות אירועי התחזוקה והעלות הכוללת לכל דגם רכב, וממיינת את התוצאות מהיקר ביותר לזול ביותר (ORDER BY total_spent DESC). זהו כלי ניהולי קריטי להבנת כדאיות כלכלית של דגמים ספציפיים.
SELECT 
    model, 
    COUNT(maintenance_status) AS total_maintenance_events,
    COALESCE(SUM(maintenance_cost), 0) AS total_spent  -- זה יציג 0 במקום NULL
FROM View_Fleet_Maintenance_Analytics
GROUP BY model
ORDER BY total_spent DESC;
<img width="615" height="522" alt="image" src="https://github.com/user-attachments/assets/6060236c-31ff-4175-8513-b9494c498a2a" />

## רשימת טיפולים פתוחים:
שאילתה זו מסננת מהמבט רכבים שסטטוס התחזוקה שלהם אינו 'Completed', ומציגה את הדגם והעלות המיוחסת לאותו טיפול. המטרה היא להציף דחיפות תפעולית ולטפל ברכבים שעדיין דורשים התייחסות טכנית.
SELECT model, maintenance_cost FROM View_Fleet_Maintenance_Analytics WHERE maintenance_status != 'Completed';
<img width="455" height="571" alt="image" src="https://github.com/user-attachments/assets/a06c8f30-b654-4320-bdf0-381242062ae1" />


## שלב ד׳:

## פונקציות:
## פונקצית חישוב שכר חודשי לנהג
פונקציה זו משמשת לחישוב מקיף ודינמי של שכר הנהגים בצי הרכבים עבור חודש ושנה ספציפיים (המתקבלים כפרמטרים). הפונקציה סורקת את כל הנסיעות שהושלמו באותו חודש, מחשבת את שעות העבודה של כל נהג (כולל חישוב שעות נוספות במידה ועבר את רף 160 השעות), ומחזירה טבלה מפורטת עם נתוני השכר והשעות של כל נהג פעיל.
<img width="785" height="692" alt="image" src="https://github.com/user-attachments/assets/2dca4782-24be-4718-80dd-37797604789f" />
<img width="849" height="710" alt="image" src="https://github.com/user-attachments/assets/856850a7-21e1-4b0c-8802-8569a0174b64" />
הפלט לאחר הרצת התוכנית הקוראת לפונקציה -
<img width="866" height="393" alt="image" src="https://github.com/user-attachments/assets/25484435-780b-4f46-9e1d-920f39303648" />
הפונקציה עושה שימוש באלמנטים המתקדמים הבאים:

א. Cursor – implicit and explicit
הגדרנו סמן מפורש (Explicit Cursor) בשם cur_active_drivers השולף בצורה מבוקרת את רשימת כל הנהגים שהיו פעילים בחודש המבוקש, ומאפשר לעבור עליהם אחד-אחד באמצעות פקודות פתיחה, שליפה וסגירה. בנוסף, בלולאת ה-FOR הפנימית, המערכת מריצה שאילתת SELECT ישירה על טבלת הנסיעות ומנהלת סמן משתמע (Implicit Cursor) באופן אוטומטי מאחורי הקלעים עבור נסיעותיו של כל נהג.

ב. החזרת Ref Cursor / Table
הפונקציה מוגדרת ככזו המחזירה טבלה (RETURNS TABLE). היא משתמשת בפקודת RETURN NEXT כדי לבנות ולהחזיר דינמית סט נתונים טבלאי, המדמה את ההתנהגות הדינמית של Ref Cursor, ומציג את פלט החישוב המלא עבור כל נהג שנמצאו לו שעות פעילות בחודש שנבדק.

ג. הסתעפויות
בקוד קיימות הסתעפויות מורכבות של תנאי IF-THEN-ELSE. המערכת בודקת האם סטטוס הנסיעה הוא Completed, וכן מבצעת בדיקה מתמטית האם הנהג חרג מרף 160 השעות כדי לקבוע את תעריף השעה שלו, תעריף רגיל של 50 שקלים לעומת תעריף שעות נוספות מוגדל ב-125 אחוזים.

ד. לולאות
הפונקציה משלבת לולאה בתוך לולאה (Nested Loops). קיימת לולאת LOOP חיצונית שעוברת על הנהגים הפעילים שהתקבלו מהסמן המפורש עד להגעה לתנאי העצירה EXIT WHEN NOT FOUND, ולולאת FOR פנימית שסורקת ומסכמת את כל שעות הנסיעה האינדיבידואליות של נהג ספציפי באותו חודש.

ה. חריגות
בסוף הפונקציה מוגדר בלוק EXCEPTION חכם עם תפיסת שגיאות כללית באמצעות WHEN OTHERS THEN. במידה ותתרחש תקלה לא צפויה בזמן הריצה, המערכת תתפוס את השגיאה בצורה מבוקרת, תמנע קריסה של התוכנית הראשית, ותדפיס פלט מסודר עם סיבת התקלה באמצעות SQLERRM.

ו. רשומות
נעשה שימוש במשתני רשומה דינמיים מסוג RECORD בשמות v_driver_record ו-v_trip_record. משתנים אלו מאפשרים להחזיק שורות נתונים שלמות ומגוונות מתוך הטבלאות השונות, ולגשת לשדות שלהן בצורה נוחה וישירה במהלך הריצה.

## פונקציה לניהול מצב הרכבים לפי רבעון
פונקציה זו משמשת להפקת דוח ניהולי פיננסי ותפעולי מקיף עבור כל רכב בצי הרכבים, לפי רבעון ושנה ספציפיים המתקבלים כפרמטרים. הפונקציה מחשבת ומסכמת עבור כל רכב את סך הוצאות הדלק, עלויות התחזוקה והטיפולים, וסך שעות הנסיעה שבוצעו בפועל במהלך הרבעון. על בסיס הנתונים הללו, הפונקציה מנתחת ומסווגת אוטומטית את סטטוס היעילות של הרכב ומחזירה מצביע לתוצאות.
<img width="961" height="683" alt="image" src="https://github.com/user-attachments/assets/af00d25d-79a4-46f7-b043-1b25838801a8" />
<img width="996" height="596" alt="image" src="https://github.com/user-attachments/assets/f96b0bf0-42bc-44d5-9c71-a25d470c5567" />
הפלט לאחר הרצת התוכנית הקוראת לפונקציה -
<img width="1150" height="363" alt="image" src="https://github.com/user-attachments/assets/8ae6b9c1-56b9-4ed2-925c-950261b9f3d7" />

הפונקציה עושה שימוש באלמנטים המתקדמים הבאים:

א. Cursor – implicit and explicit
בתוך הפונקציה הגדרנו ועשינו שימוש בסמן מפורש (Explicit Cursor) מבוסס משתנה בשם v_report_cursor. במקום להחזיר את כל סט הנתונים ישירות לזיכרון בבת אחת, הקוד פותח את הסמן (OPEN FOR) עבור שאילתת הניתוח המורכבת, מה שמציע ניהול זיכרון יעיל ומבוקר של הנתונים ברמת השרת.

ב. החזרת Ref Cursor / Table
הפונקציה מוגדרת בצורה מתקדמת ככזו המחזירה טיפוס מסוג refcursor. היא מייצרת ומחזירה באופן דינמי מצביע ישיר (Pointer) לסט התוצאות, המאפשר לתוכנית הראשית שמפעילה אותה לשלוף ולדפדף בין השורות של הדוח בצורה מבוזרת וחכמה.

ג. הסתעפויות
בקוד ממומשת הסתעפות מורכבת של תנאים בעזרת מבנה CASE-WHEN-ELSE. המערכת מנתחת את היחס בין סך ההוצאות לבין שעות השימוש ברכב על הכביש ומסווגת את הרכב לאחד משלושה סטטוסים: רכב לא יעיל עם הוצאות גבוהות ושימוש נמוך, רכב עם הוצאות גבוהות אך שימוש גבוה, או רכב יעיל ותקין.

ד. חריגות
בסוף הפונקציה מוגדר בלוק EXCEPTION חכם עם תפיסת שגיאות כללית באמצעות WHEN OTHERS THEN. במידה ותתרחש תקלה לא צפויה בזמן עיבוד הנתונים הפיננסיים, המערכת תתפוס את השגיאה בצורה מבוקרת, תדפיס פלט מסודר עם סיבת התקלה באמצעות SQLERRM, ותחזיר ערך ריק (NULL) כדי למנוע את קריסת התוכנית הראשית.

ה. רשומות
נעשה שימוש במשתנה רשומה דינמי מסוג refcursor להחזקת מצביע שורות הנתונים המורכבות המיוצרות מהחיבור בין שלוש תת-שאילתות שונות (טבלת דלק, טבלת תחזוקה וטבלת נסיעות), מה שמאפשר לטפל במבנה השורות המגוון של הדוח בצורה גמישה.
