import psycopg2
from psycopg2 import Error

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="level4",
        user="shoham",
        password="shoham"
    )

def fetch_detailed_data(entity_name):
    conn = get_db_connection()
    cur = conn.cursor()
    
    queries = {
        "Customer": "SELECT id, phonenumber, email, fullname FROM public.customer ORDER BY id;",
        "Driver": "SELECT driverid, firstname, lastname, phone, licensenumber, licensetype, hiredate, city, status FROM public.driver ORDER BY driverid;",
        "Vehicle": "SELECT vehicleid, licenseplate, vehicletype, capacity, manufacturer, year, model, carcolor, status FROM public.vehicle ORDER BY vehicleid;",
        "Route": "SELECT origin, destination, distancekm, estimatedtraveltime FROM public.route;",
        "Trip": """
            SELECT t.tripid, t.departuretime, t.status, 
                   d.firstname || ' ' || d.lastname AS driver, 
                   v.manufacturer || ' ' || v.model AS vehicle,
                   c.fullname AS customer,
                   t.price, t.numofpassengers, t.route_origin, t.route_destination
            FROM public.trip t
            LEFT JOIN public.driver d ON t.driverid = d.driverid
            LEFT JOIN public.vehicle v ON t.vehicleid = v.vehicleid
            LEFT JOIN public.customer c ON t.customer_id = c.id
            ORDER BY t.tripid;
        """,
        "Fuel Log": """
            SELECT f.fuellogid, f.fuellogdate, f.fuelamount, f.fuelcost, f.fuelstation,
                   v.model AS vehicle, d.firstname AS driver
            FROM public.fuellog f
            LEFT JOIN public.vehicle v ON f.vehicleid = v.vehicleid
            LEFT JOIN public.driver d ON f.driverid = d.driverid
            ORDER BY f.fuellogid;
        """,
        "Insurance": """
            SELECT i.insuranceid, i.insurancecompany, i.policynumber, i.startdate, i.enddate, i.cost,
                   v.model AS vehicle
            FROM public.insurance i
            LEFT JOIN public.vehicle v ON i.vehicleid = v.vehicleid
            ORDER BY i.insuranceid;
        """,
        "Maintenance": """
            SELECT m.maintenanceid, m.maintenancedate, m.maintenancetype, m.cost, m.notes,
                   v.model AS vehicle, m.maintenance_status
            FROM public.maintenance m
            LEFT JOIN public.vehicle v ON m.vehicleid = v.vehicleid
            ORDER BY m.maintenanceid;
        """
    }
    
    cur.execute(queries[entity_name])
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def fetch_dashboard_stats():
    conn = get_db_connection()
    stats = {
        "total_vehicles": 0, "active_vehicles": 0, 
        "maintenance_vehicles": 0, "total_drivers": 0, 
        "total_trips": 0
    }
    if not conn: return stats
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM public.vehicle;")
        stats["total_vehicles"] = cur.fetchone()[0]
        # במקום השורה הקודמת, השתמש בזו:
        cur.execute("SELECT COUNT(*) FROM public.vehicle WHERE TRIM(LOWER(status)) = 'active';")
        stats["active_vehicles"] = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM public.vehicle WHERE status = 'maintenance' OR status = 'broken';")
        stats["maintenance_vehicles"] = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM public.driver;")
        stats["total_drivers"] = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM public.trip;")
        stats["total_trips"] = cur.fetchone()[0]
        cur.close()
    except Exception as e:
        print("Dashboard Error:", e)
    finally:
        if conn: conn.close()
        
    return stats

def fetch_single_record(table_name, pk_col, pk_val, fields):
    conn = get_db_connection()
    cur = conn.cursor()
    fields_str = ", ".join(fields)
    query = f"SELECT {fields_str} FROM {table_name} WHERE {pk_col} = %s;"
    cur.execute(query, (pk_val,))
    record = cur.fetchone()
    cur.close()
    conn.close()
    return record

def delete_record_db(table_name, pk_col, pk_val):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f"DELETE FROM {table_name} WHERE {pk_col} = %s;"
    cur.execute(query, (pk_val,))
    conn.commit()
    cur.close()
    conn.close()

def insert_record_db(table_name, fields, values):
    conn = get_db_connection()
    cur = conn.cursor()
    placeholders = ", ".join(["%s"] * len(fields))
    cols = ", ".join(fields)
    query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders});"
    cur.execute(query, tuple(values))
    conn.commit()
    cur.close()
    conn.close()

def update_record_db(table_name, pk_col, pk_val, fields, values):
    conn = get_db_connection()
    cur = conn.cursor()
    set_clause = ", ".join([f"{f} = %s" for f in fields])
    query = f"UPDATE {table_name} SET {set_clause} WHERE {pk_col} = %s;"
    values.append(pk_val)
    cur.execute(query, tuple(values))
    conn.commit()
    cur.close()
    conn.close()

# ==========================================
# FUNCTIONS FOR STORED PROCEDURES
# ==========================================

def run_calc_salaries(month, year):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM public.fn_calculate_all_drivers_salaries(%s, %s);", (month, year))
    columns = [desc[0] for desc in cur.description]
    data = cur.fetchall()
    cur.close()
    conn.close()
    return columns, data

def run_efficiency_report(quarter, year):
    conn = get_db_connection()
    cur = conn.cursor()
    # Refcursor requires fetching within the same transaction block
    cur.execute("BEGIN;")
    cur.execute("SELECT public.fn_get_vehicle_efficiency_report(%s, %s);", (quarter, year))
    cursor_name = cur.fetchone()[0]
    
    cur.execute(f'FETCH ALL FROM "{cursor_name}";')
    columns = [desc[0] for desc in cur.description]
    data = cur.fetchall()
    
    cur.execute("COMMIT;")
    cur.close()
    conn.close()
    return columns, data

def run_assign_vehicle_to_trip(trip_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL public.assign_vehicle_to_trip(%s);", (trip_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def run_close_month_maintenance(max_mileage):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL public.close_month_maintenance_mileage(%s);", (max_mileage,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()