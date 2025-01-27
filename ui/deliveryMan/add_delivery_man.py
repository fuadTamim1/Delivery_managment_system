import tkinter as tk
from tkinter import ttk, filedialog
from .DeliveryMan import add_delivery_man, vehicle_types

def page_add_delivery_man(self):
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Add Delivery Man")

    # First Field: Name
    tk.Label(page, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    self.delivery_name_entry = ttk.Entry(page)
    self.delivery_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

    # Second Field: Vehicle (Dropdown)
    tk.Label(page, text="Vehicle:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    self.vehicle_var = tk.StringVar(value="Select Vehicle")
    vehicle_options = vehicle_types
    self.vehicle_dropdown = ttk.Combobox(page, values=vehicle_options, textvariable=self.vehicle_var, state="readonly")
    self.vehicle_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    # Add Delivery Man Button
    tk.Button(page, text="Add Delivery Man", command=lambda: add_delivery_man(self)).grid(row=2, column=0, columnspan=2, pady=20)

# Note: Ensure the `add_delivery_man` function handles the `name` and `vehicle` values properly.
