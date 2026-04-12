from db import engine
from sqlalchemy import text
from datetime import date, timedelta
import random

maintenance_types = [
    "Oil Change",
    "Tires",
    "Brakes",
    "Engine",
    "Inspection",
    "Battery",
    "Air Conditioning"
]

notes_options = [
    "Routine service",
    "Replaced parts",
    "Brake fix",
    "Engine repair",
    "General inspection",
    "Preventive maintenance",
    "Urgent repair"
]

start_maintenance_id = 921
num_rows = 100

vehicle_ids = list(range(1, 621))

maintenances = []

base_date = date(2024, 1, 1)

for i in range(num_rows):
    maintenance_id = start_maintenance_id + i

    maintenance_date = base_date + timedelta(days=random.randint(0, 800))

    maintenance_type = random.choice(maintenance_types)

    # מחירי בסיס לפי הדאטה שלך
    if maintenance_type == "Oil Change":
        cost = 500.00
    elif maintenance_type == "Tires":
        cost = 800.00
    elif maintenance_type == "Brakes":
        cost = 600.00
    elif maintenance_type == "Engine":
        cost = 1200.00
    else:
        cost = round(random.uniform(300, 1500), 2)

    notes = random.choice(notes_options)

    vehicle_id = random.choice(vehicle_ids)

    maintenances.append({
        "MaintenanceID": maintenance_id,
        "MaintenanceDate": maintenance_date,
        "MaintenanceType": maintenance_type,
        "Cost": cost,
        "Notes": notes,
        "VehicleID": vehicle_id
    })

with engine.begin() as connection:
    connection.execute(
        text("""
            INSERT INTO MAINTENANCE
            (MaintenanceID, MaintenanceDate, MaintenanceType, Cost, Notes, VehicleID)
            VALUES
            (:MaintenanceID, :MaintenanceDate, :MaintenanceType, :Cost, :Notes, :VehicleID)
        """),
        maintenances
    )

print("100 MAINTENANCE rows inserted successfully!")