import tkinter as tk
from tkinter import ttk
import os
from ui.deliveryMan.view_delivery_men_table import page_view_delivery_men
from ui.deliveryMan.add_delivery_man import page_add_delivery_man
from ui.workRecord.view_work_records import page_view_work_records
from ui.workRecord.add_work_record import page_add_work_record
from ui.account.view_accounts import page_view_accounts
from ui.account.add_account import page_add_account
from ui.admin_panel import control_panel
from database.connection import setup_database
import path

import sv_ttk

class DeliveryERMApp:
    def __init__(self, root):
        self.root_path = os.path.dirname(os.path.abspath(__file__))
        self.root = root
        path.init_folder()
        setup_database(self)
        
        self.root.title("Delivery Management System")
        self.window_width = 800
        self.window_height = 600
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.position_x = (self.screen_width // 2) - (self.window_width // 2)
        self.position_y = (self.screen_height // 2) - (self.window_height // 2)
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.position_x}+{self.position_y}")
        
        
        self.enableResizableX = False
        self.enableResizableY = True
        # Disable window resizing
        self.root.resizable(True, True)

        # self.root.geometry("900x600")
        self.delivery_men = []  # List to store delivery men data
        # self.work_records_table # List to store delivery men data
        self.setup_ui()

    def setup_ui(self):
        """Setup the main UI components."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        
        # Pages setup
        # delivery man pages
        page_view_delivery_men(self)
        page_add_delivery_man(self)
        
        # work record pages
        page_view_work_records(self)
        page_add_work_record(self)
        
        # account pages
        page_add_account(self)
        page_view_accounts(self)
        
        # admin page
        control_panel(self)
        
        sv_ttk.set_theme("dark")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = DeliveryERMApp(root)
    root.mainloop()
