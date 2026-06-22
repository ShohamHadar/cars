import customtkinter as ctk
from tkinter import ttk, messagebox
import database as db

class OperationsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("System Operations & Procedures")
        self.geometry("900x600")
        self.transient(parent)
        self.grab_set()

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.tab_salaries = self.tabview.add("Driver Salaries")
        self.tab_efficiency = self.tabview.add("Vehicle Efficiency")
        self.tab_close_month = self.tabview.add("Close Month Maintanance")

        self.build_salaries_tab()
        self.build_efficiency_tab()
        # self.build_assign_tab() - מחקתי את הקריאה הזו כי היא לא הייתה מוגדרת והייתה קורסת
        self.build_close_month_tab()

    # ==============================================================
    # 1. פונקציית שכר הנהגים
    # ==============================================================
    def build_salaries_tab(self):
        top_frame = ctk.CTkFrame(self.tab_salaries, fg_color="transparent")
        top_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(top_frame, text="Month (1-12):").pack(side="left", padx=5)
        self.entry_month = ctk.CTkEntry(top_frame, width=60)
        self.entry_month.pack(side="left", padx=5)
        self.entry_month.insert(0, "4")

        ctk.CTkLabel(top_frame, text="Year:").pack(side="left", padx=5)
        self.entry_year = ctk.CTkEntry(top_frame, width=80)
        self.entry_year.pack(side="left", padx=5)
        self.entry_year.insert(0, "2026")

        ctk.CTkButton(top_frame, text="Calculate Salaries", command=self.run_salaries, fg_color="#17a2b8").pack(side="left", padx=20)

        self.tree_salaries = ttk.Treeview(self.tab_salaries, show='headings')
        self.tree_salaries.pack(fill='both', expand=True, pady=10)

    def run_salaries(self):
        month = self.entry_month.get()
        year = self.entry_year.get()
        if not month or not year:
            messagebox.showwarning("Input Error", "Please provide month and year.")
            return
            
        try:
            columns, data = db.run_calc_salaries(int(month), int(year))
            self.update_tree(self.tree_salaries, columns, data)
        except Exception as e:
            messagebox.showerror("Execution Error", f"Failed to calculate salaries:\n{e}")

    # ==============================================================
    # 2. פונקציית יעילות רכבים
    # ==============================================================
    def build_efficiency_tab(self):
        top_frame = ctk.CTkFrame(self.tab_efficiency, fg_color="transparent")
        top_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(top_frame, text="Quarter (1-4):").pack(side="left", padx=5)
        self.entry_q = ctk.CTkEntry(top_frame, width=60)
        self.entry_q.pack(side="left", padx=5)
        self.entry_q.insert(0, "1")

        ctk.CTkLabel(top_frame, text="Year:").pack(side="left", padx=5)
        self.entry_q_year = ctk.CTkEntry(top_frame, width=80)
        self.entry_q_year.pack(side="left", padx=5)
        self.entry_q_year.insert(0, "2026")

        ctk.CTkButton(top_frame, text="Run Efficiency Report", command=self.run_efficiency, fg_color="#17a2b8").pack(side="left", padx=20)

        self.tree_efficiency = ttk.Treeview(self.tab_efficiency, show='headings')
        self.tree_efficiency.pack(fill='both', expand=True, pady=10)

    def run_efficiency(self):
        q = self.entry_q.get()
        year = self.entry_q_year.get()
        try:
            columns, data = db.run_efficiency_report(int(q), int(year))
            self.update_tree(self.tree_efficiency, columns, data)
        except Exception as e:
            messagebox.showerror("Execution Error", f"Failed to run report:\n{e}")

 
    # ==============================================================
    # 4. פרוצדורת סגירת חודש / קילומטראז'
    # ==============================================================
    def build_close_month_tab(self):
        frame = ctk.CTkFrame(self.tab_close_month)
        frame.pack(pady=40, padx=40, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Run End of Month Mileage Check", font=("Arial", 18, "bold")).pack(pady=20)
        ctk.CTkLabel(frame, text="Enter the maximum allowed mileage before triggering maintenance:").pack(pady=5)
        
        self.entry_mileage = ctk.CTkEntry(frame, width=150)
        self.entry_mileage.pack(pady=10)
        self.entry_mileage.insert(0, "100.00")
        
        ctk.CTkButton(frame, text="Execute Procedure", fg_color="#ffc107", text_color="black", command=self.run_close_month).pack(pady=20)

    def run_close_month(self):
        max_m = self.entry_mileage.get()
        if not max_m: return
        try:
            db.run_close_month_maintenance(float(max_m))
            messagebox.showinfo("Success", f"Procedure executed successfully!\nVehicles exceeding {max_m} km had 'Oil Change' records automatically opened.\n\nCheck the 'Manage Maintenance' screen to view new records.")
        except Exception as e:
            messagebox.showerror("Procedure Error", f"Failed to execute procedure:\n{e}")

    # פונקציית עזר לעדכון הטבלאות הדינמיות
    def update_tree(self, tree, columns, data):
        tree.delete(*tree.get_children())
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col.upper())
            tree.column(col, width=120, anchor="center")
            
        for row in data:
            tree.insert('', 'end', values=row)