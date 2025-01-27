from tkinter import messagebox
import tkinter as tk
import database.delivery_men as d
import database.work_records as w

vehicle_types = ["Car", "Motorbike", "Bicycle", "Scooter"]

def add_delivery_man(self):
    """Add a new delivery man to the database."""
    name = self.delivery_name_entry.get()
    vehicle = self.vehicle_var.get()

    # Validate inputs
    if not name or vehicle == "Select Vehicle":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        # Assuming `d.create` is a function to save the data
        d.create(name, vehicle)

        messagebox.showinfo("Success", "Delivery man added successfully!")

        # Clear the input fields
        self.delivery_name_entry.delete(0, tk.END)
        self.vehicle_var.set("Select Vehicle")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    update_delivery_men_table(self)
    update_delivery_dropdown(self, d.get_delivery_men(), d.get_delivery_men_ids())


def update_delivery_men_table(self, data=["empty"]):
    """Fetch delivery men data from the database and update the table."""

    if data == ["empty"]:
        rows = d.all()
    else:
        rows = data

    # Clear existing rows in the Treeview
    for row in self.delivery_men_table.get_children():
        self.delivery_men_table.delete(row)

    # Insert new rows into the Treeview
    for row in rows:
        self.delivery_men_table.insert("", "end", values=row)


def get_delivery_men_names():
    # print("data", d.get_delivery_men())
    return d.get_delivery_men()

def get_delivery_name_by_Work_record(work_record_id):
    work_record = w.get(work_record_id)
    return d.nameOf(work_record[0])

def get_delivery_men_ids():
    # print("data", d.get_delivery_men_ids())
    return d.get_delivery_men_ids()


def fill_delivery_man_fields(id):
    """Fill the delivery man form fields with data from the database."""
    man = d.get(id)
    return man


def update_delivery_man(self, delivery_man_id):
    """Update delivery man details in the database."""
    name = self.update_name_entry.get()
    vehicle = self.update_vehicle_var.get()

    if not all([name, vehicle]) or vehicle == "Select Vehicle":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        # Assuming `d.update` is a function to update the data
        d.update(name, vehicle, delivery_man_id)

        messagebox.showinfo("Success", "Delivery man updated successfully!")
        # Optionally, switch back to another page or refresh details
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    # Return to the main page
    self.notebook.forget(self.notebook.index("current"))
    update_delivery_men_table(self)


def update_delivery_dropdown(self, new_names, new_ids):
    """
    Update the account dropdown with new values.

    Args:
        new_names (list): A list of new delivery names strings.
        new_ids (list): A list of new delivery IDs corresponding to the names.
    """
    # Update the accounts dictionary
    self.delivery_men = dict(zip(new_names, new_ids))
    self.delivery_names = new_names

    # Update the dropdown values
    self.delivery_man_dropdown["values"] = self.delivery_names

    # Reset the selected value
    if self.delivery_names:
        self.delivery_man_var.set(
            self.delivery_names[0]
        )  # Set to the first email by default
    else:
        self.delivery_man_var.set("Select")
