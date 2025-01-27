import tkinter as tk
from tkinter import ttk, filedialog,messagebox
from .Account import fill_account_fields, update_account

def page_update_account(self, account_id):
    """Create a page for updating Account details."""
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Update Account", state="hidden")
    # self.notebook.select(page)

    form_labels = ["Email:", "Password:", "Place:"]
    self.update_form = {}

    # Fetch current details from the database
    delivery_man = fill_account_fields(account_id)

    if not delivery_man:
        messagebox.showerror("Error", "Account not found!")
        return

    # Fill form with current data
    for idx, label in enumerate(form_labels):
        tk.Label(page, text=label).grid(row=idx, column=0, padx=10, pady=10, sticky='e')
        entry = ttk.Entry(page)
        entry.grid(row=idx, column=1, padx=10, pady=10, sticky='w')
        entry.insert(0, delivery_man[idx])  # Prefill with existing data
        self.update_form[label[:-1].lower()] = entry

    # Update Button
    tk.Button(page, text="Update Account", 
              command=lambda: update_account(self,account_id)).grid(row=5, column=0, columnspan=3, pady=20)
