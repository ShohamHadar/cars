from db import engine
from sqlalchemy import text
from datetime import date, timedelta
import random

first_names = ["John", "David", "Michael", "Daniel", "Sarah", "Noa", "Liam", "Amit", "Eden", "Maya"]
last_names = ["Cohen", "Levi", "Mizrahi", "Peretz", "Goldberg", "Adams", "Brown", "Smith", "Katz", "Dayan"]
license_types = ["A", "B", "C", "D"]

start_id = 521

drivers = []

for i in range(100):
    driver_id = start_id + i

    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = "05" + "".join([str(random.randint(0, 9)) for _ in range(8)])  # 10-11 ספרות

    license_number = 100521 + i  # ייחודי (חייב להיות UNIQUE)

    license_type = random.choice(license_types)

    hire_date = date(2020, 1, 1) + timedelta(days=random.randint(0, 1500))

    drivers.append({
        "DriverID": driver_id,
        "FirstName": first,
        "LastName": last,
        "Phone": phone,
        "LicenseNumber": license_number,
        "LicenseType": license_type,
        "HireDate": hire_date
    })

with engine.begin() as connection:
    connection.execute(
        text("""
            INSERT INTO DRIVER
            (DriverID, FirstName, LastName, Phone, LicenseNumber, LicenseType, HireDate)
            VALUES
            (:DriverID, :FirstName, :LastName, :Phone, :LicenseNumber, :LicenseType, :HireDate)
        """),
        drivers
    )

print("100 DRIVER rows inserted successfully!")
