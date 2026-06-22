import customtkinter as ctk
from tkinter import ttk, messagebox, simpledialog
import database as db
from reports import ReportsWindow
from operations import OperationsWindow

ctk.set_appearance_mode("light")

TABLE_CONFIGS = {
    "Customer": {
        "table": "public.customer", "pk": "id",
        "columns": ["ID", "Phone", "Email", "Full Name"],
        "fields": ["phonenumber", "email", "fullname"]
    },
    "Driver": {
        "table": "public.driver", "pk": "driverid",
        "columns": ["ID", "First Name", "Last Name", "Phone", "License #", "License Type", "Hire Date", "City", "Status"],
        "fields": ["firstname", "lastname", "phone", "licensenumber", "licensetype", "hiredate", "city", "status"]
    },
    "Vehicle": {
        "table": "public.vehicle", "pk": "vehicleid",
        "columns": ["ID", "Plate", "Type", "Capacity", "Manufacturer", "Year", "Model", "Color", "Status"],
        "fields": ["licenseplate", "vehicletype", "capacity", "manufacturer", "year", "model", "carcolor", "status"]
    },
    "Route": {
        "table": "public.route", "pk": "origin",
        "columns": ["Origin", "Destination", "Distance (km)", "Est. Time (min)"],
        "fields": ["origin", "destination", "distancekm", "estimatedtraveltime"]
    },
    "Trip": {
        "table": "public.trip", "pk": "tripid",
        "columns": ["ID", "Departure", "Status", "Driver", "Vehicle", "Customer", "Price", "Passengers", "Origin", "Destination"],
        "fields": ["departuretime", "status", "driverid", "vehicleid", "price", "numofpassengers", "durationhours", "customer_id", "route_origin", "route_destination"]
    },
    "Fuel Log": {
        "table": "public.fuellog", "pk": "fuellogid",
        "columns": ["ID", "Date", "Amount", "Cost", "Station", "Vehicle", "Driver"],
        "fields": ["fuellogdate", "fuelamount", "fuelcost", "fuelstation", "vehicleid", "driverid"]
    },
    "Insurance": {
        "table": "public.insurance", "pk": "insuranceid",
        "columns": ["ID", "Company", "Policy #", "Start Date", "End Date", "Cost", "Vehicle"],
        "fields": ["insurancecompany", "policynumber", "startdate", "enddate", "cost", "vehicleid"]
    },
    "Maintenance": {
        "table": "public.maintenance", "pk": "maintenanceid",
        "columns": ["ID", "Date", "Type", "Cost", "Notes", "Vehicle", "Status"],
        "fields": ["maintenancedate", "maintenancetype", "cost", "notes", "vehicleid", "maintenance_status"]
    }
}

class CRUDWindow(ctk.CTkToplevel):
    def __init__(self, parent, entity_name):
        super().__init__(parent)
        self.entity_name = entity_name
        self.cfg = TABLE_CONFIGS[entity_name]
        
        self.AUTO_INCREMENT_TABLES = ["Customer", "Driver", "Vehicle", "Trip", "Fuel Log", "Insurance", "Maintenance"]
        
        self.title(f"Manage {entity_name}")
        self.geometry("950x550")
        self.transient(parent)
        self.grab_set()

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=10, padx=10, fill="x")

        ctk.CTkButton(self.top_frame, text="Refresh Data", command=self.load_data).pack(side="left", padx=5)
        ctk.CTkButton(self.top_frame, text="Add Record", fg_color="#28a745", command=self.open_add_form).pack(side="left", padx=5)
        ctk.CTkButton(self.top_frame, text="Update via ID", fg_color="#fd7e14", command=self.open_update_prompt).pack(side="left", padx=5)
        ctk.CTkButton(self.top_frame, text="Delete Selected", fg_color="#dc3545", command=self.delete_selected).pack(side="right", padx=5)

        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.tree = ttk.Treeview(self.tree_frame, columns=self.cfg["columns"], show='headings')
        for col in self.cfg["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110, anchor="center")
            
        self.tree.column(self.cfg["columns"][0], width=0, stretch=False)
            
        yscroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        yscroll.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=yscroll.set)
        self.tree.pack(fill='both', expand=True)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            data = db.fetch_detailed_data(self.entity_name)
            for row in data:
                self.tree.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load data:\n{e}")

    def get_next_id(self):
        try:
            conn = db.get_db_connection()
            cur = conn.cursor()
            query = f"SELECT COALESCE(MAX({self.cfg['pk']}), 0) + 1 FROM {self.cfg['table']};"
            cur.execute(query)
            next_id = cur.fetchone()[0]
            cur.close()
            conn.close()
            return next_id
        except Exception as e:
            print(f"Error calculating next ID: {e}")
            return None

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a row from the table to delete.")
            return
        
        record_id = self.tree.item(selected[0])['values'][0]
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete this record?"):
            try:
                db.delete_record_db(self.cfg["table"], self.cfg["pk"], record_id)
                messagebox.showinfo("Success", "Record deleted.")
                self.load_data()
            except Exception as e:
                messagebox.showerror("Error", f"Delete failed:\n{e}")

    def open_update_prompt(self):
        pk_val = simpledialog.askstring("Update Record", f"Enter {self.cfg['pk']} to update:")
        if not pk_val: return
        
        try:
            record = db.fetch_single_record(self.cfg["table"], self.cfg["pk"], pk_val, self.cfg["fields"])
            if not record:
                messagebox.showerror("Error", "Record ID not found.")
                return
            self.open_form(mode="UPDATE", pk_val=pk_val, existing_data=record)
        except Exception as e:
            messagebox.showerror("Error", f"Fetch failed:\n{e}")

    def open_add_form(self):
        self.open_form(mode="ADD")

    def open_form(self, mode, pk_val=None, existing_data=None):
        form = ctk.CTkToplevel(self)
        form.title(f"{mode} {self.entity_name}")
        form.geometry("400x550")
        
        form.transient(self)   
        form.lift()            
        form.grab_set()        

        ctk.CTkLabel(form, text=f"{mode} {self.entity_name}", font=("Arial", 18, "bold")).pack(pady=15)
        
        scroll_frame = ctk.CTkScrollableFrame(form)
        # התיקון הקריטי: yard=10 שונה ל- pady=10 כדי שהחלון לא יישבר
        scroll_frame.pack(fill="both", expand=True, padx=15, pady=10)

        entries = {}
        for i, field in enumerate(self.cfg["fields"]):
            ctk.CTkLabel(scroll_frame, text=f"{field.replace('_', ' ').upper()}:").pack(anchor="w", padx=10, pady=2)
            entry = ctk.CTkEntry(scroll_frame, width=280)
            entry.pack(pady=5, padx=10)
            
            if mode == "UPDATE" and existing_data:
                if existing_data[i] is not None:
                    entry.insert(0, str(existing_data[i]))
            entries[field] = entry

        def save():
            try:
                # הפיכת מחרוזת ריקה או רווחים ל-None בצורה בטוחה
                values = [entries[f].get().strip() if entries[f].get().strip() != "" else None for f in self.cfg["fields"]]
                
                if mode == "ADD":
                    if self.entity_name in self.AUTO_INCREMENT_TABLES:
                        generated_id = self.get_next_id()
                        if generated_id is None:
                            messagebox.showerror("Error", "Could not generate automatic ID.")
                            return
                        
                        final_fields = [self.cfg["pk"]] + self.cfg["fields"]
                        final_values = [generated_id] + values
                        db.insert_record_db(self.cfg["table"], final_fields, final_values)
                    else:
                        db.insert_record_db(self.cfg["table"], self.cfg["fields"], values)
                else:
                    db.update_record_db(self.cfg["table"], self.cfg["pk"], pk_val, self.cfg["fields"], values)
                
                messagebox.showinfo("Success", "Database updated successfully.")
                form.destroy()
                self.load_data()
            except Exception as e:
                messagebox.showerror("Database Error", f"Operation failed:\n{e}")

        ctk.CTkButton(form, text="Save Changes", fg_color="#28a745", command=save).pack(pady=15)


class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FleetManager - Dashboard")
        self.geometry("1000x650")
        
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="right", fill="y")
        
        self.main_area = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_area.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # ====== Sidebar ======
        ctk.CTkLabel(self.sidebar, text="FleetManager", font=("Arial", 22, "bold")).pack(pady=(20, 30))
        
        self.card_labels = {}

        for entity in TABLE_CONFIGS.keys():
            btn = ctk.CTkButton(self.sidebar, text=f"Manage {entity}", fg_color="transparent", 
                                text_color="black", hover_color="#e0e0e0",
                                anchor="e", command=lambda ent=entity: self.open_crud_window(ent))
            btn.pack(pady=5, padx=20, fill="x")
            
        btn_reports = ctk.CTkButton(self.sidebar, text="Reports & Analysis", fg_color="#4b0082", 
                                    text_color="white", anchor="center", command=self.open_reports)
        btn_reports.pack(pady=(20, 10), padx=20, fill="x")
        
        btn_ops = ctk.CTkButton(self.sidebar, text="System Operations", fg_color="#0056b3", 
                                text_color="white", anchor="center", command=self.open_operations)
        btn_ops.pack(pady=(5, 10), padx=20, fill="x")

        # ====== Dashboard Area ======
        ctk.CTkLabel(self.main_area, text="System Dashboard", font=("Arial", 28, "bold")).pack(anchor="e", pady=(0, 20))
        
        self.cards_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.cards_frame.pack(fill="both", expand=True)
        
        self.cards_frame.grid_columnconfigure(0, weight=1)
        self.cards_frame.grid_columnconfigure(1, weight=1)

        self.refresh_dashboard()

    def create_card(self, parent, title, value, row, col):
        card = ctk.CTkFrame(parent, height=130, corner_radius=15, fg_color="#ffffff", border_width=1, border_color="#cccccc")
        card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        card.grid_propagate(False)
        ctk.CTkLabel(card, text=title, font=("Arial", 18, "bold"), text_color="#555555").pack(pady=(20, 10))
        
        val_label = ctk.CTkLabel(card, text=str(value), font=("Arial", 36, "bold"), text_color="black")
        val_label.pack()
        self.card_labels[title] = val_label

    def refresh_dashboard(self, event=None):
        try:
            stats = db.fetch_dashboard_stats()
            
            if self.card_labels:
                self.card_labels["Total Vehicles"].configure(text=str(stats["total_vehicles"]))
                self.card_labels["Active Vehicles"].configure(text=str(stats["active_vehicles"]))
                self.card_labels["Registered Drivers"].configure(text=str(stats["total_drivers"]))
                self.card_labels["In Maintenance"].configure(text=str(stats["maintenance_vehicles"]))
                self.card_labels["Total Trips"].configure(text=str(stats["total_trips"]))
            else:
                self.create_card(self.cards_frame, "Total Vehicles", stats["total_vehicles"], row=0, col=1)
                self.create_card(self.cards_frame, "Active Vehicles", stats["active_vehicles"], row=0, col=0)
                self.create_card(self.cards_frame, "Registered Drivers", stats["total_drivers"], row=1, col=1)
                self.create_card(self.cards_frame, "In Maintenance", stats["maintenance_vehicles"], row=1, col=0)
                self.create_card(self.cards_frame, "Total Trips", stats["total_trips"], row=2, col=1)
        except Exception as e:
            print(f"Error refreshing dashboard: {e}")

    def open_crud_window(self, entity_name):
        crud_win = CRUDWindow(self, entity_name)
        crud_win.bind("<Destroy>", self.refresh_dashboard)

    def open_reports(self):
        ReportsWindow(self)
        
    def open_operations(self):
        OperationsWindow(self)

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()