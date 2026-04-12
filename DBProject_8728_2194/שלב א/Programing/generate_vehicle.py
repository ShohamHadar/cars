from db import engine
from sqlalchemy import text
import random

vehicle_types = ["Taxi", "Van", "Minibus", "Bus"]
manufacturers = ["Toyota", "Mercedes", "Kia", "Hyundai", "Ford", "Volvo", "Isuzu", "Renault"]

start_vehicle_id = 521
start_license_plate = 1111631

vehicles = []

for i in range(100):
    vehicle_id = start_vehicle_id + i
    license_plate = start_license_plate + i

    vehicle_type = random.choice(vehicle_types)
    manufacturer = random.choice(manufacturers)

    # קיבולת לפי הדאטה שלך בפועל (בערכים ריאליים בלבד, בלי מבנה מורכב)
    if vehicle_type == "Taxi":
        capacity = 4
    elif vehicle_type == "Van":
        capacity = random.randint(6, 10)
    elif vehicle_type == "Minibus":
        capacity = random.randint(10, 20)
    else:  # Bus
        capacity = random.randint(40, 60)

    model = random.randint(2018, 2024)
    year = model  # לפי הדאטה שלך זה זהה

    vehicles.append({
        "VehicleID": vehicle_id,
        "LicensePlate": license_plate,
        "VehicleType": vehicle_type,
        "Capacity": capacity,
        "Manufacturer": manufacturer,
        "Model": model,
        "Year": year
    })

with engine.begin() as connection:
    connection.execute(
        text("""
            INSERT INTO VEHICLE
            (VehicleID, LicensePlate, VehicleType, Capacity, Manufacturer, Model, Year)
            VALUES
            (:VehicleID, :LicensePlate, :VehicleType, :Capacity, :Manufacturer, :Model, :Year)
        """),
        vehicles
    )

print("100 VEHICLE rows inserted successfully!")