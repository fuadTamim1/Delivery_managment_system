import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

import database.delivery_men as deliveryMan
from .DeliveryMan import update_delivery_men_table
from .edit_delivery_man import page_update_delivery_man
def page_view_delivery_men(self):
    """Create the UI for managing delivery men."""    
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Manage Delivery Men")
    # self.notebook.select(page)
    
    # Create a frame for the search bar and date selection
    search_frame = ttk.Frame(page)
    search_frame.pack(pady=10)

    # Search bar
    search_label = ttk.Label(search_frame, text="Search for user:")
    search_label.grid(row=0, column=0, padx=5)
    search_entry = ttk.Entry(search_frame)
    search_entry.grid(row=0, column=1, padx=5)

    # Search button
    search_button = ttk.Button(search_frame, text="Search", command=lambda: filter_delivery_men(search_entry.get()))
    search_button.grid(row=0, column=6, padx=5)

    clear_button = ttk.Button(search_frame, text="Clear", command=lambda: reset_search())
    # clear_button.pack_forget()

    # Create the Treeview table
    cols = ["id","name","vehicle"]
    total_columns = len(cols)
    self.delivery_men_table = ttk.Treeview(
        page, columns=(cols), show="headings"
    )
    self.delivery_men_table.pack(fill="both", expand=True, padx=10, pady=10)
    # Set the headings for the columns
    for col in cols:
        self.delivery_men_table.heading(col, text=col.capitalize())
        self.delivery_men_table.column(col, width=int(900 / total_columns), stretch=True)

    # Fetch delivery men data from the database and populate the table
    update_delivery_men_table(self)

    def filter_delivery_men(user_search):
        self.result = deliveryMan.filter_delivery_men(user_search)
        if(user_search == ""):
            clear_button.grid_remove()
        else:
            clear_button.grid(row=0, column=7, padx=5)
        update_delivery_men_table(self, self.result)
        print(self.result)
    
    def reset_search():
        search_entry.delete(0,tk.END)
        update_delivery_men_table(self)
        
    def show_context_menu(event):
        item_id = self.delivery_men_table.identify_row(event.y)
        if item_id:
            context_menu = tk.Menu(self.root, tearoff=0)
            context_menu.add_command(label="Edit", command=lambda: edit_row(item_id))
            context_menu.add_command(label="Delete", command=lambda: delete_row(item_id))
            context_menu.post(event.x_root, event.y_root)

    def edit_row(item_id):
        values = self.delivery_men_table.item(item_id)["values"]
        page_update_delivery_man(self, values[0])
        print("Editing:", values)

    def delete_row(item_id):
        values = self.delivery_men_table.item(item_id)["values"]
        if not messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete record with ID {values[0]}?"):
            return
        print("Deleting:", values)
        deliveryMan.delete(values[0])
        messagebox.showinfo("Success", "Delivery account has been deleted successfully!")
        update_delivery_men_table(self)

    self.delivery_men_table.bind("<Button-3>", show_context_menu)
