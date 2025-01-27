import tkinter as tk
from tkinter import ttk, filedialog,messagebox
from .DeliveryMan import fill_delivery_man_fields, update_delivery_man, vehicle_types

def page_update_delivery_man(self, delivery_man_id):
    """Create a page for updating delivery man details."""
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Update Delivery Man", state="hidden")
    self.notebook.select(page)

    # Fetch current details from the database
    delivery_man = fill_delivery_man_fields(delivery_man_id)

    if not delivery_man:
        messagebox.showerror("Error", "Delivery man not found!")
        return

    # Create and prefill the "Name" field
    tk.Label(page, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    self.update_name_entry = ttk.Entry(page)
    self.update_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    self.update_name_entry.insert(0, delivery_man[0])  # Prefill with existing name

    # Create the "Vehicle" dropdown
    tk.Label(page, text="Vehicle:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    self.update_vehicle_var = tk.StringVar(value=delivery_man[1])  # Prefill with existing vehicle
    self.update_vehicle_dropdown = ttk.Combobox(
        page, textvariable=self.update_vehicle_var, state="readonly",
        values=vehicle_types
    )
    self.update_vehicle_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    # Update Button
    tk.Button(
        page, text="Update Delivery Man", 
        command=lambda: update_delivery_man(self, delivery_man_id)
    ).grid(row=5, column=0, columnspan=3, pady=20)
