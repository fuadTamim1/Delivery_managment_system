import tkinter as tk
from tkinter import ttk, messagebox
import database.work_records as w
from .WorkRecord import update_work_records_table
from .edit_work_record import page_update_work_record
from tkcalendar import DateEntry
import utils.helper as h


def page_view_work_records(self):
    """Create the UI for managing work records."""
    page = ttk.Frame(self.notebook)
    self.notebook.add(page, text="Manage Work Record")

    cols = [
        "id",
        "delivery_man_name",
        "account",
        "orders_count",
        "tips",
        "date",
        "shift",
        "confirmation_photo",
    ]
    total_columns = len(cols)

    # Create a frame for the search bar and date selection
    search_frame = ttk.Frame(page)
    search_frame.pack(pady=10)

    # Search bar
    search_label = ttk.Label(search_frame, text="Search for user:")
    search_label.grid(row=0, column=0, padx=5)
    search_entry = ttk.Entry(search_frame)
    search_entry.grid(row=0, column=1, padx=5)

    # Date selection
    from_label = ttk.Label(search_frame, text="From:")
    from_label.grid(row=0, column=2, padx=5)
    from_date = DateEntry(search_frame)
    from_date.grid(row=0, column=3, padx=5)

    to_label = ttk.Label(search_frame, text="To:")
    to_label.grid(row=0, column=4, padx=5)
    to_date = DateEntry(search_frame)
    to_date.grid(row=0, column=5, padx=5)
    from_date.get(), to_date.get()
    # Search button
    search_button = ttk.Button(
        search_frame,
        text="Search",
        command=lambda: filter_work_records(search_entry.get()),
    )
    search_button.grid(row=0, column=6, padx=5)

    clear_button = ttk.Button(
        search_frame, text="Clear", command=lambda: reset_search()
    )
    # clear_button.pack_forget()

    # Create the Treeview table
    self.work_records_table = ttk.Treeview(
        page,
        columns=(cols),
        show="headings",
    )
    self.work_records_table.pack(fill="both", expand=True, padx=2, pady=10)

    # Set the headings for the columns
    # for col in ["delivery_man_id", "", "orders_count", "date", "shift", "confirmation_photo"]:
    #     self.work_records_table.heading(col, text=col.capitalize())

    for col in cols:
        self.work_records_table.heading(col, text=col.capitalize())
        self.work_records_table.column(
            col, width=int(900 / total_columns), stretch=True
        )
        # self.work_records_table.column(col, width=100, stretch=True)
    # Ensure the table is updated after creating it
    update_work_records_table(self)

    def filter_work_records(user_search):
        f_start_date = h.get_formatted_date(from_date.get_date())
        f_end_date = h.get_formatted_date(to_date.get_date())
        if not h.compare_dates(f_start_date, f_end_date):
            messagebox.showwarning(
                "filter failed",
                message="From date field must be older or equal to To date.",
            )
            return
        result = w.filter_work_records(user_search, f_start_date, f_end_date)
        if user_search == "":
            clear_button.grid_remove()
        else:
            clear_button.grid(row=0, column=7, padx=5)
        update_work_records_table(self, result)
        print(result)

    def reset_search():
        search_entry.delete(0, tk.END)
        update_work_records_table(self)

    def show_context_menu(event):
        item_id = self.work_records_table.identify_row(event.y)
        if item_id:
            context_menu = tk.Menu(self.root, tearoff=0)
            context_menu.add_command(label="Edit", command=lambda: edit_row(item_id))
            context_menu.add_command(
                label="Delete", command=lambda: delete_row(item_id)
            )
            context_menu.post(event.x_root, event.y_root)

    def edit_row(item_id):
        values = self.work_records_table.item(item_id)["values"]
        page_update_work_record(self, values)
        print("Editing:", values)

    def delete_row(item_id):
        values = self.work_records_table.item(item_id)["values"]
        if not messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete record with ID {values[0]}?",
        ):
            return
        print("Deleting:", values)
        w.delete(values[0])
        messagebox.showinfo("Success", "Record has deleted succfully!")
        update_work_records_table(self)

    self.work_records_table.bind("<Button-3>", show_context_menu)  # Right-click binding
