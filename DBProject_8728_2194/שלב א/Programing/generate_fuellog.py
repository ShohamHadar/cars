from db import engine
from sqlalchemy import text
from datetime import date, timedelta
import random

fuel_stations = [
    "Paz", "Delek", "Sonol", "Yellow", "Ten", "Dor Alon"
]

start_fuel_log_id = 521
num_rows = 20000  

driver_ids = list(range(1, 621))
vehicle_ids = list(range(1, 621))

fuel_logs = []

base_date = date(2023, 1, 1)

for i in range(num_rows):
    fuel_log_id = start_fuel_log_id + i

    fuel_date = base_date + timedelta(days=random.randint(0, 800))

    fuel_amount = round(random.uniform(20, 120), 2)

    fuel_cost = round(fuel_amount * random.uniform(5.5, 8.5), 2)

    station = random.choice(fuel_stations)

    vehicle_id = random.choice(vehicle_ids)
    driver_id = random.choice(driver_ids)

    fuel_logs.append({
        "FuelLogID": fuel_log_id,
        "FuelLogDate": fuel_date,
        "FuelAmount": fuel_amount,
        "FuelCost": fuel_cost,
        "FuelStation": station,
        "VehicleID": vehicle_id,
        "DriverID": driver_id
    })

batch_size = 1000

with engine.begin() as connection:
    for i in range(0, num_rows, batch_size):
        batch = fuel_logs[i:i + batch_size]

        connection.execute(
            text("""
                INSERT INTO FUELLOG
                (FuelLogID, FuelLogDate, FuelAmount, FuelCost, FuelStation, VehicleID, DriverID)
                VALUES
                (:FuelLogID, :FuelLogDate, :FuelAmount, :FuelCost, :FuelStation, :VehicleID, :DriverID)
            """),
            batch
        )

print("20,000 FUELLOG rows inserted successfully!")