import tkinter as tk
from tkinter import ttk, messagebox
import database.accounts as a
import database.work_records as w
from utils.validation import is_valid_email

def add_account(self):
    email = self.account_form["email"].get()
    password = self.account_form["password"].get()
    place = self.account_form["place"].get()

    if not all([email, password, place]):
        messagebox.showerror("Error", "All fields are required!")
        return
    if is_valid_email(email):
        a.create(email, password, place)
    else:
        messagebox.showwarning("Warning", "The email that your entered is not valid!")
        return
    messagebox.showinfo("Success", "Account added successfully!")

    # Update the account men table after adding a new account man
    for field in self.account_form.values():
        field.delete(0, tk.END)
    update_accounts_table(self)
    update_account_dropdown(self,a.get_emails(), a.get_accounts_ids())
     
def update_accounts_table(self, data = ["empty"]):
    """Fetch account men data from the database and update the table."""

    if(data == ["empty"]):
        rows = a.all()
    else:
        rows = data
    
    # Clear existing rows in the Treeview
    for row in self.accounts_table.get_children():
        self.accounts_table.delete(row)

    # Insert new rows into the Treeview
    for row in rows:
        self.accounts_table.insert("", "end", values=row)

def get_accounts_emails():
    # print("data",a.get_accounts())
    return a.get_emails()

def get_account_email_by_Work_record(work_record_id):
    work_record = w.get(work_record_id)
    return a.emailOf(work_record[1])

def get_accounts_ids():
    # print("data",a.get_accounts_ids())
    return a.get_accounts_ids()

def fill_account_fields(id): 
    """Fill the account form fields with data from the database."""
    account = a.get(id)
    return account
    
def update_account(self, account_id):
    """Update account details in the database."""
    email = self.update_form['email'].get()
    password = self.update_form['password'].get()
    place = self.update_form['place'].get()

    if not all([email, password, place]):
        messagebox.showerror("Error", "All fields are required!")
        return

    a.update(email, password, place, account_id)
    
    messagebox.showinfo("Success", "Account updated successfully!")

    # Return to the main page
    self.notebook.forget(self.notebook.index("current"))
    update_accounts_table(self)

def update_account_dropdown(self, new_emails, new_ids):
    """
    Update the account dropdown with new values.
    
    Args:
        new_emails (list): A list of new account email strings.
        new_ids (list): A list of new account IDs corresponding to the emails.
    """
    # Update the accounts dictionary
    self.accounts = dict(zip(new_emails, new_ids))
    self.account_emails = new_emails

    # Update the dropdown values
    self.account_dropdown['values'] = self.account_emails
    
    # Reset the selected value
    if self.account_emails:
        self.account_var.set(self.account_emails[0])  # Set to the first email by default
    else:
        self.account_var.set("Select")