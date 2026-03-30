import csv
import random
from datetime import datetime, timedelta

NUM_LOGS = 20000
START_ID = 521

MAX_DRIVER_ID = 520
MAX_VEHICLE_ID = 520

stations = ["Paz", "Sonol", "Delek", "Ten", "Dor Alon"]

start_date = datetime(2024, 2, 1)

with open("fuellog_20000.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "FuelLogID", "FuelLogDate", "FuelAmount",
        "FuelCost", "FuelStation", "VehicleID", "DriverID"
    ])

    for i in range(NUM_LOGS):
        log_id = START_ID + i

        amount = random.uniform(20, 70)
        price = random.uniform(6.5, 8.5)
        cost = amount * price

        fuel_date = start_date + timedelta(days=i % 365)

        writer.writerow([
            log_id,
            fuel_date.strftime("%Y-%m-%d"),
            f"{amount:.2f}",
            f"{cost:.2f}",
            random.choice(stations),
            random.randint(1, MAX_VEHICLE_ID),
            random.randint(1, MAX_DRIVER_ID)
        ])

print("fuellog_20000.csv created")
