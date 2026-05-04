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
<img width="296" height="168" alt="image" src="https://github.com/user-attachments/assets/e0f2f77d-4a73-4d26-955d-e29ff611c4ab" />
בדיקה לאחר commit -
<img width="293" height="164" alt="image" src="https://github.com/user-attachments/assets/0ebc6f89-3fc7-4209-b738-a96a9f7295c0" />


## שאילתות update ושימוש בcommit -
עדכון סטטוס תחזוקה ״בתהליך״ לטיפולים שהתאריך שלהם הוא מה-30 ימים האחרונים ועד היום:
<img width="736" height="273" alt="image" src="https://github.com/user-attachments/assets/26c53a8c-c5e6-45f6-9736-f6fa94e9fb9a" />

הכנסת נתונים לעמודת עיר בטבלת נהגים:
<img width="1310" height="241" alt="image" src="https://github.com/user-attachments/assets/bac5e72d-4096-4374-9a81-cc4bd79df2d5" />

שידוך בין ביטוח לרכב על מנת להבטיח שלכל רכב יהיה ביטוח אחד בלבד:
<img width="744" height="434" alt="image" src="https://github.com/user-attachments/assets/00660380-51b5-468a-a8ea-eccc4e180d2f" />

עדכון מחיר נסיעה לפי סוג רכב -
<img width="859" height="401" alt="image" src="https://github.com/user-attachments/assets/d68d9f41-3005-472a-bed4-b5cda968b8af" />
