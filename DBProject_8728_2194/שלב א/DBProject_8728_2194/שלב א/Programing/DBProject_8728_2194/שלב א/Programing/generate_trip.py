import csv
import random
from datetime import datetime, timedelta

NUM_TRIPS = 20000
START_ID = 521   # כי יש כבר עד 520

MAX_DRIVER_ID = 520
MAX_VEHICLE_ID = 520

locations = [
    "Jerusalem","Tel Aviv","Haifa","Ashdod","Beer Sheva",
    "Netanya","Holon","Raanana","Tiberias","Safed",
    "Nazareth","Eilat","Ashkelon","Herzliya","Bat Yam"
]

start_time = datetime(2024, 2, 1, 6, 0, 0)

with open("trip_20000.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "TripID","DepartureLocation","Destination",
        "DepartureTime","Status","DriverID","VehicleID"
    ])

    for i in range(NUM_TRIPS):
        trip_id = START_ID + i

        dep = random.choice(locations)
        dest = random.choice([x for x in locations if x != dep])

        time = start_time + timedelta(minutes=i*30)

        writer.writerow([
            trip_id,
            dep,
            dest,
            time.strftime("%Y-%m-%d %H:%M:%S"),
            random.choice(["true","false"]),
            random.randint(1, MAX_DRIVER_ID),
            random.randint(1, MAX_VEHICLE_ID)
        ])

print("trip_20000.csv created")
