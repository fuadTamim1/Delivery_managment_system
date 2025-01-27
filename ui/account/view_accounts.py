import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

import database.accounts as account
from .Account import update_accounts_table
from .edit_account import page_update_account
def page_view_accounts(self):
    """Create the UI for managing accounts."""    
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Accounts")
    # self.notebook.select(page)
    
    # Create a frame for the search bar and date selection
    search_frame = ttk.Frame(page)
    search_frame.pack(pady=10)

    # Search bar
    search_label = ttk.Label(search_frame, text="Search for email:")
    search_label.grid(row=0, column=0, padx=5)
    search_entry = ttk.Entry(search_frame)
    search_entry.grid(row=0, column=1, padx=5)

    search_button = ttk.Button(search_frame, text="Search", command=lambda: filter_accounts(search_entry.get()))
    search_button.grid(row=0, column=6, padx=5)

    clear_button = ttk.Button(search_frame, text="Clear", command=lambda: reset_search())
    # clear_button.pack_forget()

    # Create the Treeview table
    cols = ["id","email", "place"]
    total_columns = len(cols)
    self.accounts_table = ttk.Treeview(
        page, columns=(cols), show="headings"
    )
    self.accounts_table.pack(fill="both", expand=True, padx=10, pady=10)
    # Set the headings for the columns
    for col in cols:
        self.accounts_table.heading(col, text=col.capitalize())
        self.accounts_table.column(col, width=int(900 / total_columns), stretch=True)

    # Fetch accounts data from the database and populate the table
    update_accounts_table(self)

    def filter_accounts(user_search):
        self.result = account.filter_accounts(user_search)
        if(user_search == ""):
            clear_button.grid_remove()
        else:
            clear_button.grid(row=0, column=7, padx=5)
        update_accounts_table(self, self.result)
        print(self.result)
    
    def reset_search():
        search_entry.delete(0,tk.END)
        update_accounts_table(self)
        
    def show_context_menu(event):
        item_id = self.accounts_table.identify_row(event.y)
        if item_id:
            context_menu = tk.Menu(self.root, tearoff=0)
            context_menu.add_command(label="Edit", command=lambda: edit_row(item_id))
            context_menu.add_command(label="Delete", command=lambda: delete_row(item_id))
            context_menu.post(event.x_root, event.y_root)

    def edit_row(item_id):
        values = self.accounts_table.item(item_id)["values"]
        page_update_account(self, values[0])
        print("Editing:", values)

    def delete_row(item_id):
        values = self.accounts_table.item(item_id)["values"]
        if not messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete record with ID {values[0]}?"):
            return
        print("Deleting:", values)
        account.delete(values[0])
        messagebox.showinfo("Success", "Account has been deleted successfully!")
        update_accounts_table(self)

    self.accounts_table.bind("<Button-3>", show_context_menu)
