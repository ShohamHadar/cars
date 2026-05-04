-- =========================================
-- VEHICLE
-- =========================================

-- מחיקת עמודת מודל
ALTER TABLE Vehicle
DROP COLUMN Model;

-- אילוצים
ALTER TABLE Vehicle
ADD CONSTRAINT chk_vehicle_capacity_positive
CHECK (Capacity > 0);

ALTER TABLE Vehicle
ADD CONSTRAINT chk_vehicle_type
CHECK (VehicleType IN ('Bus', 'Minibus', 'Van', 'Taxi'));

-- =========================================
-- DRIVER
-- =========================================

-- הוספת עמודת עיר
ALTER TABLE Driver 
ADD COLUMN City VARCHAR(50);

-- אילוצים
ALTER TABLE Driver
ADD CONSTRAINT chk_driver_license_type
CHECK (LicenseType IN ('A','B', 'C', 'D'));

ALTER TABLE Driver
ADD CONSTRAINT chk_driver_phone_length
CHECK (Phone LIKE '05%' AND LENGTH(Phone) = 10);

ALTER TABLE Driver
ADD CONSTRAINT chk_driver_hire_date
CHECK (HireDate <= CURRENT_DATE);

-- =========================================
-- TRIP
-- =========================================

-- הוספת עמודות
ALTER TABLE Trip 
ADD COLUMN Price NUMERIC(10, 2) DEFAULT 0;

ALTER TABLE Trip 
ADD COLUMN NumOfPassengers INT DEFAULT 1;

ALTER TABLE Trip 
ADD COLUMN DurationHours NUMERIC(4, 2);

-- עדכון המפתח זר המקשר בין טבלת רכב לטבלת נסיעה
ALTER TABLE trip DROP CONSTRAINT trip_vehicleid_fkey;
ALTER TABLE trip ADD CONSTRAINT trip_vehicleid_fkey 
FOREIGN KEY (vehicleid) REFERENCES vehicle(vehicleid) ON DELETE CASCADE;

-- אילוצים
ALTER TABLE Trip
ADD CONSTRAINT chk_trip_price_non_negative
CHECK (Price >= 0);

ALTER TABLE Trip
ADD CONSTRAINT chk_trip_passengers_positive
CHECK (NumOfPassengers > 0);

ALTER TABLE Trip
ADD CONSTRAINT chk_trip_duration_positive
CHECK (DurationHours > 0);

-- =========================================
-- FUELLOG
-- =========================================
--עדכון מפתח זר בין טבלת רכב לטבלת תדלוק
ALTER TABLE fuellog DROP CONSTRAINT IF EXISTS fuellog_vehicleid_fkey;
ALTER TABLE fuellog ADD CONSTRAINT fuellog_vehicleid_fkey 
FOREIGN KEY (vehicleid) REFERENCES vehicle(vehicleid) ON DELETE CASCADE;

-- אילוצים
ALTER TABLE FuelLog
ADD CONSTRAINT chk_fuel_amount_positive
CHECK (FuelAmount > 0);

ALTER TABLE FuelLog
ADD CONSTRAINT chk_fuel_cost_positive
CHECK (FuelCost > 0);

-- =========================================
-- MAINTENANCE
-- =========================================

-- הוספת עמודת סטטוס
ALTER TABLE Maintenance 
ADD COLUMN maintenance_status VARCHAR(20) 
DEFAULT 'Scheduled'
CHECK (maintenance_status IN ('Scheduled', 'In Progress', 'Completed', 'Cancelled'));

-- עדכון המפתח זר המקשר בין טבלת רכב לטבלת תחזוקה
ALTER TABLE maintenance DROP CONSTRAINT IF EXISTS maintenance_vehicleid_fkey;
ALTER TABLE maintenance ADD CONSTRAINT maintenance_vehicleid_fkey 
FOREIGN KEY (vehicleid) REFERENCES vehicle(vehicleid) ON DELETE CASCADE;

-- אילוצים
ALTER TABLE Maintenance
ADD CONSTRAINT chk_maintenance_cost_non_negative
CHECK (Cost >= 0);

ALTER TABLE Maintenance
ADD CONSTRAINT chk_maintenance_type
CHECK (MaintenanceType IN ('Oil Change', 'Tires', 'Brakes', 'Engine', 'Inspection', 'Air Conditioning', 'Battery'));

-- =========================================
-- INSURANCE
-- =========================================

-- עדכון המפתח זר המקשר בין טבלת רכב לטבלת ביטוח
ALTER TABLE insurance DROP CONSTRAINT IF EXISTS insurance_vehicleid_fkey;
ALTER TABLE insurance ADD CONSTRAINT insurance_vehicleid_fkey 
FOREIGN KEY (vehicleid) REFERENCES vehicle(vehicleid) ON DELETE CASCADE;

-- אילוצים
ALTER TABLE Insurance
ADD CONSTRAINT chk_insurance_dates
CHECK (EndDate > StartDate);

ALTER TABLE Insurance
ADD CONSTRAINT chk_insurance_cost_positive
CHECK (Cost > 0);
