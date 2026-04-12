from db import engine
from sqlalchemy import text
from datetime import date, timedelta
import random

insurance_companies = ["Clal", "Harel", "Phoenix", "Migdal"]

start_insurance_id = 521
start_policy_number = 200521 

vehicles_ids = list(range(0, 621))  # צריך להתאים ל-VEHICLE שלך (100 רכבים)

insurances = []

for i in range(100):
    insurance_id = start_insurance_id + i

    company = random.choice(insurance_companies)

    policy_number = start_policy_number + i
   
    policy_number = start_policy_number + i

    start_date = date(2020, 1, 1) + timedelta(days=random.randint(0, 1500))
    end_date = start_date + timedelta(days=random.randint(365, 1825))  # 1–5 שנים

    cost = round(random.uniform(800, 5000), 2)

    vehicle_id = random.choice(vehicles_ids)

    insurances.append({
        "InsuranceID": insurance_id,
        "InsuranceCompany": company,
        "PolicyNumber": policy_number,
        "StartDate": start_date,
        "EndDate": end_date,
        "Cost": cost,
        "VehicleID": vehicle_id
    })

with engine.begin() as connection:
    connection.execute(
        text("""
            INSERT INTO INSURANCE
            (InsuranceID, InsuranceCompany, PolicyNumber, StartDate, EndDate, Cost, VehicleID)
            VALUES
            (:InsuranceID, :InsuranceCompany, :PolicyNumber, :StartDate, :EndDate, :Cost, :VehicleID)
        """),
        insurances
    )

print("100 INSURANCE rows inserted successfully!")