import customtkinter as ctk
from tkinter import ttk, messagebox
import database as db

# מילון שאילתות עם תבניות דינמיות
REPORT_QUERIES = {
    "Avg Maintenance Cost": {
        "description": "Average maintenance cost by vehicle type, manufacturer, and year.",
        "type": "complex",
        "query": "SELECT v.VehicleType, v.Manufacturer, v.year, COUNT(m.MaintenanceID) AS NumOfMaintenances, ROUND(AVG(m.Cost)::numeric, 2) AS AvgMaintenanceCost FROM public.Vehicle v JOIN public.Maintenance m ON v.VehicleID = m.VehicleID {where_clause} GROUP BY v.VehicleType, v.Manufacturer, v.year ORDER BY AvgMaintenanceCost DESC;"
    },
    "Above Average Maintenance": {
        "description": "Vehicles whose total maintenance cost exceeds the fleet average.",
        "type": "complex",
        "query": "SELECT v.VehicleID, v.VehicleType, v.Manufacturer, v.Year, SUM(m.Cost) AS TotalMaintenanceCost FROM public.VEHICLE v JOIN public.MAINTENANCE m ON v.VehicleID = m.VehicleID {where_clause} GROUP BY v.VehicleID, v.VehicleType, v.Manufacturer, v.Year HAVING SUM(m.Cost) > (SELECT AVG(total_cost) FROM (SELECT SUM(Cost) as total_cost FROM public.MAINTENANCE GROUP BY VehicleID) as sub) ORDER BY TotalMaintenanceCost DESC;"
    },
    "Expired Insurance": {
        "description": "Vehicles with expired or missing insurance policies.",
        "type": "simple",
        "query": "SELECT v.VehicleID, v.LicensePlate, i.EndDate FROM public.VEHICLE v LEFT JOIN public.INSURANCE i ON v.VehicleID = i.VehicleID {where_clause} ORDER BY v.VehicleID;"
    },
    "Bus Insurance by Company": {
        "description": "Average insurance costs by company.",
        "type": "simple",
        "query": "SELECT i.insurancecompany, ROUND(AVG(i.cost)::numeric, 2) AS AvgInsuranceCost FROM public.Insurance i JOIN public.Vehicle v ON i.VehicleID = v.VehicleID {where_clause} GROUP BY i.insurancecompany ORDER BY AvgInsuranceCost DESC;"
    },
    "Inactive Drivers": {
        "description": "Drivers who have not completed any trips in the selected period.",
        "type": "driver",
        "query": "SELECT d.DriverID, d.FirstName, d.LastName FROM public.Driver d WHERE NOT EXISTS (SELECT 1 FROM public.Trip t JOIN public.Vehicle v ON t.VehicleID = v.VehicleID WHERE t.DriverID = d.DriverID {time_filter} {type_filter});"
    }
}

CATEGORIES = {
    "Maintenance": ["Avg Maintenance Cost", "Above Average Maintenance"],
    "Insurance": ["Expired Insurance", "Bus Insurance by Company"],
    "Drivers": ["Inactive Drivers"]
}

class ReportsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Reports & Advanced Analytics")
        self.geometry("1100x700")
        self.transient(parent)
        self.grab_set()

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.selectors = {}
        for cat in CATEGORIES.keys():
            tab = self.tabview.add(cat)
            self.build_tab(tab, cat)

    def build_tab(self, parent, cat):
        top_bar = ctk.CTkFrame(parent, fg_color="transparent")
        top_bar.pack(fill="x", pady=10)
        
        sel = ctk.CTkOptionMenu(top_bar, values=CATEGORIES[cat], width=200)
        sel.pack(side="left", padx=5)
        
        time_sel = ctk.CTkOptionMenu(top_bar, values=["All Time", "Last Year", "Last Month"], width=120)
        time_sel.pack(side="left", padx=5)
        
        type_sel = ctk.CTkOptionMenu(top_bar, values=["All Vehicle Types", "Bus", "Minibus", "Van"], width=120)
        type_sel.pack(side="left", padx=5)
        
        ctk.CTkButton(top_bar, text="Execute & Analyze", fg_color="#28a745", 
                      command=lambda: self.run_report(cat, sel.get(), time_sel.get(), type_sel.get(), parent)).pack(side="left", padx=20)
        
        self.table_frame = ctk.CTkFrame(parent)
        self.table_frame.pack(fill="both", expand=True, pady=10)

    def run_report(self, cat, report_name, time_val, type_val, parent):
        cfg = REPORT_QUERIES[report_name]
        sql = cfg["query"]
        
        # 1. בניית תנאי הסינון הבסיסיים
        conditions = []
        if type_val != "All Vehicle Types":
            conditions.append(f"v.VehicleType = '{type_val}'")
            
        # ברירת מחדל לדוח ביטוחים פגים - תמיד יציג פגים או חסרים אלא אם סונן לפי זמן
        if report_name == "Expired Insurance" and time_val == "All Time":
            conditions.append("(i.EndDate < CURRENT_DATE OR i.VehicleID IS NULL)")

        # 2. החלת עקרון החסימה הדו-צדדית (מניעת זיוף נתונים עתידיים מה-DB)
        time_cond = ""
        
        if time_val == "Last Month":
            if cat == "Maintenance":
                conditions.append("m.MaintenanceDate >= CURRENT_DATE - INTERVAL '1 month' AND m.MaintenanceDate <= CURRENT_DATE")
            elif cat == "Insurance":
                conditions.append("i.EndDate >= CURRENT_DATE - INTERVAL '1 month' AND i.EndDate <= CURRENT_DATE")
            elif cat == "Drivers":
                time_cond = "t.DepartureTime >= CURRENT_DATE - INTERVAL '1 month' AND t.DepartureTime <= CURRENT_DATE"
                
        elif time_val == "Last Year":
            if cat == "Maintenance":
                conditions.append("m.MaintenanceDate >= CURRENT_DATE - INTERVAL '1 year' AND m.MaintenanceDate <= CURRENT_DATE")
            elif cat == "Insurance":
                conditions.append("i.EndDate >= CURRENT_DATE - INTERVAL '1 year' AND i.EndDate <= CURRENT_DATE")
            elif cat == "Drivers":
                time_cond = "t.DepartureTime >= CURRENT_DATE - INTERVAL '1 year' AND t.DepartureTime <= CURRENT_DATE"

        # 3. הזרקה חכמה לפי סוג הדוח המקורי שלך
        if cfg["type"] == "complex":
            where = "WHERE " + " AND ".join(conditions) if conditions else ""
            sql = sql.format(where_clause=where)
        elif cfg["type"] == "simple":
            where = "WHERE " + " AND ".join(conditions) if conditions else ""
            sql = sql.format(where_clause=where)
        elif cfg["type"] == "driver":
            t_f = f"AND {time_cond}" if time_cond else ""
            type_f = f"AND v.VehicleType = '{type_val}'" if type_val != "All Vehicle Types" else ""
            sql = sql.format(time_filter=t_f, type_filter=type_f)

        # הרצה והצגה ב-Treeview
        try:
            conn = db.get_db_connection()
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            cols = [desc[0].upper() for desc in cur.description]
            
            # ניקוי הטבלה הקודמת
            for w in parent.winfo_children():
                if isinstance(w, ctk.CTkFrame) and w != parent.winfo_children()[0]:
                    w.destroy()
            
            table_cont = ctk.CTkFrame(parent)
            table_cont.pack(fill="both", expand=True)
            tree = ttk.Treeview(table_cont, columns=cols, show='headings')
            for c in cols: tree.heading(c, text=c); tree.column(c, width=120)
            for row in data: tree.insert('', 'end', values=row)
            tree.pack(fill='both', expand=True)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))