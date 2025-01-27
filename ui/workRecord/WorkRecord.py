import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import database.work_records as w
import uuid
import os
from shutil import copy2
from path import get_media_folder_path


def add_work_record(self):
    selected_delivery_name = self.delivery_man_var.get()  # Get the selected name
    selected_delivery_id = self.delivery_men.get(
        selected_delivery_name
    )  # Get the corresponding ID
    print(
        f"Selected Name: {selected_delivery_name}, Selected ID: {selected_delivery_id}"
    )
    delivery_man = selected_delivery_id

    selected_account_email = self.account_var.get()  # Get the selected name
    selected_account_id = self.accounts.get(
        selected_account_email
    )  # Get the corresponding ID
    print(
        f"Selected Name: {selected_account_email}, Selected ID: {selected_account_id}"
    )
    account = selected_account_id

    tips = self.tips_entry.get()
    orders_count = self.orders_count_entry.get()
    date = self.date_var.get()
    shift_from = f"{self.shift_from_hour_var.get()}:{self.shift_from_min_var.get()} {self.shift_from_am_pm_var.get()}"
    shift_to = f"{self.shift_to_hour_var.get()}:{self.shift_to_min_var.get()} {self.shift_to_am_pm_var.get()}"
    confirmation_photo_temp = self.confirmation_photo_var.get()
    confirmation_photo = ""

    if not all([delivery_man, account, tips, orders_count, date, shift_from, shift_to]):
        messagebox.showerror("Error", "All fields are required!")
        return

    if not all([confirmation_photo_temp]):
        if messagebox.askyesno(
            "no confirmation photo provided.",
            message="are you sure you won't to upload an confirmation photo for work record?",
        ):
            pass
        else:
            return
    else:
        confirmation_photo = upload_file(
            confirmation_photo_temp,
            "delivery men",
            f"{selected_delivery_id}_{selected_delivery_name}",
        )
        confirmation_photo = upload_file(
            confirmation_photo_temp,
            "accounts",
            f"{selected_account_id}_{selected_account_email}",
        )

    w.create(
        delivery_man,
        account,
        tips,
        orders_count,
        date,
        shift_from,
        shift_to,
        confirmation_photo,
    )

    messagebox.showinfo("Success", "Work record added successfully!")

    update_work_records_table(self)

    self.delivery_man_var.set("")
    self.tips_entry.delete(0, tk.END)
    self.orders_count_entry.delete(0, tk.END)
    self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
    self.shift_from_hour_var.set("12")
    self.shift_from_min_var.set("00")
    self.shift_from_am_pm_var.set("AM")
    self.shift_to_hour_var.set("12")
    self.shift_to_min_var.set("00")
    self.shift_to_am_pm_var.set("AM")
    self.confirmation_photo_var.set("")


def update_work_records_table(self, data=["empty"]):
    """Fetch work records data from the database and update the table."""
    # Ensure the table exists before updating it
    if not hasattr(self, "work_records_table"):
        return  # Exit early if the table hasn't been created yet
    if data == ["empty"]:
        rows = (
            w.get_records_with_delivery_name()
        )  # Use the new function to get records with delivery names
    else:
        rows = data

    # Clear any existing rows in the Treeview
    for row in self.work_records_table.get_children():
        self.work_records_table.delete(row)

    # Insert new rows into the Treeview
    for row in rows:
        self.work_records_table.insert("", "end", values=row)


def fill_work_record_fields(id):
    """Fill the delivery man form fields with data from the database."""
    man = w.get(id)
    return man


def update_work_record(self, work_record_id):
    """Update work record details in the database."""
    selected_delivery_name = self.delivery_man_var.get()  # Get the selected name
    selected_delivery_id = self.delivery_men.get(
        selected_delivery_name
    )  # Get the corresponding ID
    print(
        f"Selected Name: {selected_delivery_name}, Selected ID: {selected_delivery_id}"
    )
    
    delivery_man = selected_delivery_id
    
    selected_account_email = self.account_var.get()  # Get the selected name
    selected_account_id = self.accounts.get(
        selected_account_email
    )  # Get the corresponding ID
    print(
        f"Selected Email: {selected_account_email}, Selected ID: {selected_account_id}"
    )
    account = selected_account_id
    orders_count = self.orders_count_entry.get()
    tips = self.tips_entry.get()
    date = self.date_entry.get()

    # Retrieve shift times
    shift_from_hour = self.shift_from_hour_var.get()
    shift_from_min = self.shift_from_min_var.get()
    shift_from_am_pm = self.shift_from_am_pm_var.get()
    shift_from = f"{shift_from_hour}:{shift_from_min} {shift_from_am_pm}"

    shift_to_hour = self.shift_to_hour_var.get()
    shift_to_min = self.shift_to_min_var.get()
    shift_to_am_pm = self.shift_to_am_pm_var.get()
    shift_to = f"{shift_to_hour}:{shift_to_min} {shift_to_am_pm}"

    photo_path = self.update_photo_path_var.get()

    # Validation: Ensure all fields are filled
    if not all(
        [delivery_man,account, tips, orders_count, date, shift_from, shift_to, photo_path]
    ):
        messagebox.showerror("Error", "All fields are required!")
        return

    # Update the database record
    w.update(
        delivery_man,
        account,
        orders_count,
        tips,
        date,
        shift_from,
        shift_to,
        photo_path,
        work_record_id,
    )

    messagebox.showinfo("Success", "Work record updated successfully!")

    # Close the current page and refresh the records table
    self.notebook.forget(self.notebook.index("current"))
    update_work_records_table(self)



def ensure_directory_exists(path):
    """
    Ensure that the directory at the given path exists. If it doesn't, create it.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")


def join_paths(*paths):
    """Join paths, ignoring empty or None values."""
    return os.path.join(*(p for p in paths if p))


# Function to store the file in the media folder and rename it
def upload_file(file_path, dir1="", dir2=""):
    # Open file dialog and let user choose a file
    # file_path =filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])

    if not file_path:
        messagebox.showwarning("file does not exist", "Please select a file.")
        return

    # Create media folder if it doesn't exist
    media_folder = get_media_folder_path()
    if not os.path.exists(media_folder):
        os.makedirs(media_folder)

    requested_path = join_paths(media_folder, dir1, dir2)
    ensure_directory_exists(requested_path)
    # Get file extension
    original_file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_path)[1]

    prefix_name = original_file_name

    # Generate a unique ID-based file name
    # unique_filename = prefix_name + str(uuid.uuid4()) + file_extension
    # Example: e.g., '7f3dcb49-8fa7-4b6a-b70a-6a57d7e2f57b.png'
    unique_filename = f"{prefix_name}_{uuid.uuid4()}{file_extension}"
    # print(unique_filename)
    # Create the new file path in the media folder

    new_file_path = os.path.join(requested_path, unique_filename)

    # Move and rename the file
    copy2(file_path, new_file_path)

    # Return the path to the file
    messagebox.showinfo("File Saved", f"File has been saved as: {new_file_path}")
    return new_file_path


def create_shift_selector_frame(self, parent):
    """Creates a reusable shift selector widget."""
    frame = ttk.Frame(parent)
    
    # Dropdowns for "Shift From"
    ttk.Label(frame, text="From:").grid(row=0, column=0, padx=5, pady=5)
    ttk.Combobox(frame, values=self.hours, textvariable=self.shift_from_hour_var, width=4).grid(row=0, column=1, padx=5)
    ttk.Combobox(frame, values=self.minutes, textvariable=self.shift_from_min_var, width=4).grid(row=0, column=2, padx=5)
    ttk.Combobox(frame, values=self.am_pm, textvariable=self.shift_from_am_pm_var, width=3).grid(row=0, column=3, padx=5)

    # Dropdowns for "Shift To"
    ttk.Label(frame, text="To:").grid(row=1, column=0, padx=5, pady=5)
    ttk.Combobox(frame, values=self.hours, textvariable=self.shift_to_hour_var, width=4).grid(row=1, column=1, padx=5)
    ttk.Combobox(frame, values=self.minutes, textvariable=self.shift_to_min_var, width=4).grid(row=1, column=2, padx=5)
    ttk.Combobox(frame, values=self.am_pm, textvariable=self.shift_to_am_pm_var, width=3).grid(row=1, column=3, padx=5)

    return frame