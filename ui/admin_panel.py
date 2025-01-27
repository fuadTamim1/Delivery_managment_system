import tkinter as tk
from tkinter import ttk,messagebox
import pandas as pd  # Ensure pandas is installed for Excel export
import database.work_records as w
import database.delivery_men as d
import database.accounts as a
from datetime import datetime
from path import get_excel_export_path
import os

def control_panel(self):
    # Create a new tkinter frame
    global page
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Control Panel")
    self.notebook.pack(fill="both", expand=True)
    self.notebook.select(page)

    # Assuming the page class is named `Page1` in page1.py

    # Configure the grid to make columns expand equally
    page.grid_columnconfigure(0, weight=1)  # Column 0 (left side)
    page.grid_columnconfigure(1, weight=1)  # Column 1 (right side)
    page.grid_columnconfigure(2, weight=0)  # Column for separator, no stretching

    # Add buttons for navigation with increased height
    tk.Button(
        page,
        text="View Delivery Men",
        command=lambda: view_delivery_men(self),
    ).grid(row=0, column=0, padx=20, pady=10, ipady=20, sticky="nsew")
    tk.Button(
        page, text="Add Delivery Man",bg="darkgreen", command=lambda: add_delivery_man(self)
    ).grid(row=0, column=1, padx=20, pady=10, ipady=20, sticky="nsew")
    tk.Button(
        page,
        text="View Work Records",
        command=lambda: view_work_records(self)
    ).grid(row=1, column=0, padx=20, pady=10, ipady=20, sticky="nsew")
    tk.Button(page, text="Add Work Record",bg="darkgreen", command=lambda: add_work_record(self)).grid(
        row=1, column=1, padx=20, pady=10, ipady=20, sticky="nsew"
    )
    tk.Button(
        page,
        text="View Accounts",
        command=lambda: view_accounts(self),
    ).grid(row=2, column=0, padx=20, pady=10, ipady=20, sticky="nsew")
    tk.Button(page, text="Add Account",bg="darkgreen", command=lambda: add_account(self)).grid(
        row=2, column=1, padx=20, pady=10, ipady=20, sticky="nsew"
    )

    # Create a vertical separator between columns 0 and 1
    separator = ttk.Separator(page, orient="vertical")
    separator.grid(row=0, column=2, rowspan=2, sticky="ns", padx=10)

    # Ensure the rows expand evenly
    # page.grid_rowconfigure(0, weight=1)
    # page.grid_rowconfigure(1, weight=1)
    # Ensuring equal space for the first two columns
    page.grid_columnconfigure(0, weight=1)
    page.grid_columnconfigure(1, weight=1)
    # Ensure the separator column does not stretch
    page.grid_columnconfigure(2, weight=0)

    # Export to Excel button
    def export_to_excel():
        try:
            # Fetch work records data (replace this with your data fetching logic)
            work_records_data = w.get_data_to_export()

            if not work_records_data:
                messagebox.showinfo("Info", "No work records to export.")
                return

            # Convert to pandas DataFrame and export
            df = pd.DataFrame(
                work_records_data,
                columns=[
                    "ID",
                    "Delivery Man Name",
                    "Accounts",
                    "Orders Count",
                    "Tips",
                    "Date",
                    "Shift From - To",
                ],
            )
            # Fetch work records data (replace this with your data fetching logic)
            delivery_men_data = d.all()

            if not delivery_men_data:
                messagebox.showinfo("Info", "No delivery men data to export.")
                return
            df2 = pd.DataFrame(
                delivery_men_data,
                columns=[
                    "ID",
                    "Name",
                    "Vechile Type",
                ],
            )
            
            # Fetch work records data (replace this with your data fetching logic)
            account_data = a.all()

            if not account_data:
                messagebox.showinfo("Info", "No delivery men data to export.")
                return
            df3 = pd.DataFrame(
                account_data,
                columns=[
                    "ID",
                    "Email",
                    "Place",
                ],
            )
            
            # df2 = df1.copy()
         
            file_path = os.path.join(
                get_excel_export_path(),
                f"work_records_export_{datetime.now().strftime('%Y-%m-%d')}.xlsx",
            )
            # df.to_excel(file_path, index=False)
            with pd.ExcelWriter(file_path) as writer:  
                df.to_excel(writer, sheet_name='Work_records_sheet')
                df2.to_excel(writer, sheet_name='Delivery_men_sheet')
                df3.to_excel(writer, sheet_name='Accounts_sheet')
            
            messagebox.showinfo(
                "Success", f"Work records exported successfully to {file_path}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {e}")

    tk.Button(page, text="Export Data", command=lambda: export_to_excel()).grid(
        row=3, column=0, columnspan=2, pady=20
    )


# Example methods for navigation (to be implemented in your app class)
def view_delivery_men(self):
    self.notebook.select(0)


def view_work_records(self):
    self.notebook.select(2)


def add_delivery_man(self):
    self.notebook.select(1)


def add_work_record(self):
    self.notebook.select(3)


def add_account(self):
    self.notebook.select(4)


def view_accounts(self):
    self.notebook.select(5)
