import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from .WorkRecord import fill_work_record_fields, update_work_record, create_shift_selector_frame
from ui.deliveryMan.DeliveryMan import get_delivery_men_names, get_delivery_men_ids, get_delivery_name_by_Work_record
from ui.account.Account import get_accounts_emails, get_accounts_ids, get_account_email_by_Work_record
from tkcalendar import DateEntry

def page_update_work_record(self, work_record):
    """Create a page for updating work record details."""
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Update Work Record", state="hidden")
    self.notebook.select(page)

    work_record_id = work_record[0]
    # Fetch current details from the database
    # work_record = fill_work_record_fields(work_record_id)
    print(work_record)
    if not work_record:
        messagebox.showerror("Error", "Work record not found!")
        return

    # Delivery Man Dropdown
    self.delivery_names = get_delivery_men_names()  # Get delivery man names
    self.delivery_ids = get_delivery_men_ids()      # Get delivery man IDs
    self.delivery_men = dict(zip(self.delivery_names, self.delivery_ids))
    delivery_name = get_delivery_name_by_Work_record(work_record_id)
    tk.Label(page, text="Delivery Man:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    self.delivery_man_var = tk.StringVar(value=delivery_name)
    self.delivery_man_dropdown = ttk.Combobox(
        page, values=self.delivery_names, textvariable=self.delivery_man_var, state="readonly"
    )
    self.delivery_man_dropdown.grid(row=0, column=1, padx=10, pady=10)

    # Account Dropdown
    self.account_emails = get_accounts_emails()  # Get Account emails
    self.account_ids = get_accounts_ids()        # Get Account IDs
    self.accounts = dict(zip(self.account_emails, self.account_ids))
    account_email = get_account_email_by_Work_record(work_record_id)
    tk.Label(page, text="Account:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    self.account_var = tk.StringVar(value=account_email)
    self.account_dropdown = ttk.Combobox(
        page, values=self.account_emails, textvariable=self.account_var, state="readonly"
    )
    self.account_dropdown.grid(row=1, column=1, padx=10, pady=10)

    # Orders Count
    tk.Label(page, text="Orders Count:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
    self.orders_count_entry = ttk.Entry(page)
    self.orders_count_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    self.orders_count_entry.insert(0, work_record[3])

    # Tips
    tk.Label(page, text="Tips:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
    self.tips_entry = ttk.Entry(page)
    self.tips_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    self.tips_entry.insert(0, work_record[4])

    # Date
    tk.Label(page, text="Date:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
    self.date_entry = DateEntry(page, textvariable=self.date_var, date_pattern="y-mm-dd")
    self.date_entry.grid(row=4, column=1, padx=10, pady=10)
    self.date_var.set(work_record[5])
    # Shift Selector
    
    time_string = work_record[6]

    # Split into "from" and "to" parts
    from_part, to_part = time_string.split(" - ")

    # Extract "from" hour, minute, and AM/PM
    from_time, from_am_pm = from_part.split(" ")
    from_hour, from_minute = from_time.split(":")

    # Extract "to" hour, minute, and AM/PM
    to_time, to_am_pm = to_part.split(" ")
    to_hour, to_minute = to_time.split(":")

    self.shift_from_hour_var = tk.StringVar(value=from_hour)
    self.shift_from_min_var = tk.StringVar(value=from_minute)
    self.shift_from_am_pm_var = tk.StringVar(value=from_am_pm)
    self.shift_to_hour_var = tk.StringVar(value=to_hour)
    self.shift_to_min_var = tk.StringVar(value=to_minute)
    self.shift_to_am_pm_var = tk.StringVar(value=to_am_pm)
    
    tk.Label(page, text="Shift:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
    self.shift_selector_frame = create_shift_selector_frame(self, page)
    self.shift_selector_frame.grid(row=5, column=1, padx=10, pady=10, sticky='w')

    # Confirmation Photo
    tk.Label(page, text="Confirmation Photo:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
    self.update_photo_path_var = tk.StringVar(value=work_record[7])
    photo_entry = ttk.Entry(page, textvariable=self.update_photo_path_var, state='readonly', width=40)
    photo_entry.grid(row=6, column=1, padx=10, pady=10, sticky='w')

    def select_photo():
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        self.update_photo_path_var.set(path)

    tk.Button(page, text="Choose Photo", command=select_photo).grid(row=5, column=2, padx=10, pady=10)


    # Update Button
    tk.Button(page, text="Update Work Record", 
              command=lambda: update_work_record(self, work_record_id)).grid(
        row=7, column=0, columnspan=3, pady=20)
