import tkinter as tk
from tkinter import ttk, messagebox
from .Account import add_account

def page_add_account(self):
    page = tk.Frame(self.notebook)
    self.notebook.add(page, text="Add Account")
    # self.notebook.select(page)
    form_labels = ["Email:","Password:", "Place:"]
    self.account_form = {}
        
    for idx, label in enumerate(form_labels):
        tk.Label(page, text=label).grid(row=idx, column=0, padx=10, pady=10, sticky='e')
        entry = ttk.Entry(page)
        entry.grid(row=idx, column=1, padx=10, pady=10, sticky='w')
        self.account_form[label[:-1].lower()] = entry
        
    tk.Button(page, text="Add Account", command=lambda: add_account(self)).grid(row=5, column=0, columnspan=3, pady=20)