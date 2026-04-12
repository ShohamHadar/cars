from db import engine
from sqlalchemy import text
from datetime import datetime, timedelta
import random

locations = [
    "Tel Aviv", "Jerusalem", "Haifa", "Ramat Gan", "Netanya",
    "Lod", "Petah Tikva", "Beer Sheva", "Eilat", "Ashdod"
]

start_trip_id = 521
num_rows = 20000

# לפי מה שבנית קודם:
driver_ids = list(range(1, 621))   # 100 drivers
vehicle_ids = list(range(1, 621))  # 100 vehicles

trips = []

base_time = datetime(2024, 1, 1, 6, 0, 0)

for i in range(num_rows):
    trip_id = start_trip_id + i

    departure = random.choice(locations)
    destination = random.choice(locations)

    # לוודא שלא יוצא אותו יעד ומוצא
    while destination == departure:
        destination = random.choice(locations)

    departure_time = base_time + timedelta(minutes=random.randint(0, 60 * 24 * 365))

    status = random.choice([True, False])

    driver_id = random.choice(driver_ids)
    vehicle_id = random.choice(vehicle_ids)

    trips.append({
        "TripID": trip_id,
        "DepartureLocation": departure,
        "Destination": destination,
        "DepartureTime": departure_time,
        "Status": status,
        "DriverID": driver_id,
        "VehicleID": vehicle_id
    })

# INSERT לביצוע בכמויות (יותר יעיל ל-20K)
batch_size = 1000

with engine.begin() as connection:
    for i in range(0, num_rows, batch_size):
        batch = trips[i:i + batch_size]

        connection.execute(
            text("""
                INSERT INTO TRIP
                (TripID, DepartureLocation, Destination, DepartureTime, Status, DriverID, VehicleID)
                VALUES
                (:TripID, :DepartureLocation, :Destination, :DepartureTime, :Status, :DriverID, :VehicleID)
            """),
            batch
        )

print("20,000 TRIP rows inserted successfully!")