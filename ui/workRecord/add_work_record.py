import tkinter as tk
from tkinter import ttk, filedialog

from datetime import datetime
from .WorkRecord import add_work_record, create_shift_selector_frame
from ui.deliveryMan.DeliveryMan import get_delivery_men_names, get_delivery_men_ids
from ui.account.Account import get_accounts_emails, get_accounts_ids
from tkcalendar import DateEntry

def page_add_work_record(self):
    """Create the UI for adding work records."""
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Add Work Record")
    
    
    self.delivery_names = get_delivery_men_names()  # Get delivery man names
    self.delivery_ids = get_delivery_men_ids()      # Get delivery man IDs
    # Create label
    tk.Label(page, text="Delivery Man:").grid(row=0, column=0, padx=10, pady=10)
    # Initialize StringVar for the dropdown
    # Create a dictionary mapping names to IDs
    self.delivery_men = dict(zip(self.delivery_names, self.delivery_ids))
    # print(self.delivery_names[0])
    # Initialize StringVar for the dropdown
    if self.delivery_names and self.delivery_names[0] is not None:
        first_name =  self.delivery_names[0]
    else:
        first_name = ""
    self.delivery_man_var = tk.StringVar(value=first_name)  # Default to the first name
    # Create the dropdown
    self.delivery_man_dropdown = ttk.Combobox(
        page, values=self.delivery_names, textvariable=self.delivery_man_var, state="readonly"
    )
    self.delivery_man_dropdown.grid(row=0, column=1, padx=10, pady=10)
    self.delivery_man_dropdown.set("Select")
    # Add Account Select Dropdown
    self.account_emails = get_accounts_emails()  # Get Account names
    self.account_ids = get_accounts_ids()      # Get Account IDs
    # Create label
    tk.Label(page, text="Account:").grid(row=1, column=0, padx=10, pady=10)
    # Initialize StringVar for the dropdown
    # Create a dictionary mapping names to IDs
    self.accounts = dict(zip(self.account_emails, self.account_ids))
    # print(self.account_emails[0])
    # Initialize StringVar for the dropdown
    if self.account_emails and self.account_emails[0] is not None:
        first_name =  self.account_emails[0]
    else:
        first_name = ""
    self.account_var = tk.StringVar(value=first_name)  # Default to the first name
    # Create the dropdown
    self.account_dropdown = ttk.Combobox(
        page, values=self.account_emails, textvariable=self.account_var, state="readonly"
    )
    self.account_dropdown.grid(row=1, column=1, padx=10, pady=10)
    self.account_dropdown.set("Select")
    tk.Label(page, text="Tips:").grid(row=3, column=0, padx=10, pady=10)
    self.tips_entry = ttk.Entry(page)
    self.tips_entry.grid(row=2, column=1, padx=10, pady=10)
    tk.Label(page, text="Orders Count:").grid(row=2, column=0, padx=10, pady=10)
    self.orders_count_entry = ttk.Entry(page)
    self.orders_count_entry.grid(row=3, column=1, padx=10, pady=10)
    tk.Label(page, text="Date:").grid(row=4, column=0, padx=10, pady=10)
    self.date_var = tk.StringVar()
    self.date_entry = DateEntry(page, textvariable=self.date_var, date_pattern="y-mm-dd")
    self.date_entry.grid(row=4, column=1, padx=10, pady=10)
    self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
    
    tk.Label(page, text="Shift (From - To):").grid(row=5, column=0, padx=10, pady=10)
    self.shift_from_hour_var = tk.StringVar(value="12")
    self.shift_from_min_var = tk.StringVar(value="00")
    self.shift_from_am_pm_var = tk.StringVar(value="AM")
    self.shift_to_hour_var = tk.StringVar(value="12")
    self.shift_to_min_var = tk.StringVar(value="00")
    self.shift_to_am_pm_var = tk.StringVar(value="AM")
    self.hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    self.minutes = [0, 15, 30, 45]
    self.am_pm = ["AM", "PM"]
    # Set consistent width for all Comboboxes
    self.shift_selector_frame = create_shift_selector_frame(self,page)
    self.shift_selector_frame.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(page, text="Confirmation Photo:").grid(row=6, column=0, padx=10, pady=10)
    self.confirmation_photo_var = tk.StringVar()
    confirmation_photo_entry = ttk.Entry(page, textvariable=self.confirmation_photo_var, state="readonly", width=40)
    confirmation_photo_entry.grid(row=6, column=1, padx=10, pady=10)
    def select_confirmation_photo():
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        self.confirmation_photo_var.set(path)
    tk.Button(page, text="Choose Photo", command=select_confirmation_photo).grid(row=6, column=2, padx=10, pady=10)
    tk.Button(page, text="Add Record", command=lambda: add_work_record(self)).grid(row=7, column=0, columnspan=3, pady=20)