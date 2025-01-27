import tkinter as tk
from tkinter import ttk, filedialog

def page1_update_delivery_man(self, item_id):
        page = ttk.Frame(self.notebook)
        self.notebook.add(page, text="Add Delivery Man", state="hidden")
        self.notebook.select(page)
        form_labels = ["Name:", "Email:", "Vehicle:", "Age:"]
        self.delivery_form = {}
        
        for idx, label in enumerate(form_labels):
            tk.Label(page, text=label).grid(row=idx, column=0, padx=10, pady=10, sticky='e')
            entry = ttk.Entry(page)
            entry.grid(row=idx, column=1, padx=10, pady=10, sticky='w')
            self.delivery_form[label[:-1].lower()] = entry
        
        tk.Label(page, text="Personal Photo:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.photo_path_var = tk.StringVar()
        photo_entry = ttk.Entry(page, textvariable=self.photo_path_var, state='readonly', width=40)
        photo_entry.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        
        def select_photo():
            path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
            self.photo_path_var.set(path)
        
        tk.Button(page, text="Choose Photo", command=select_photo).grid(row=4, column=2, padx=10, pady=10)
        
        tk.Button(page, text="Update Delivery Man", command=self.add_delivery_man).grid(row=5, column=0, columnspan=3, pady=20)
