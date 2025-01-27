import sqlite3
import os
import path

db_path = path.get_db_path()

def get_connection():
    """Establish and return a database connection."""
    return sqlite3.connect(db_path)

def setup_database(self):
    """Set up database in create tables if it's not exits"""
    
    try:
        # Check if the database file exists
        if not os.path.exists(db_path):
            # Create a connection to the SQLite database
            conn = sqlite3.connect(db_path)
            conn.execute("PRAGMA foreign_keys = ON;")  # Enable foreign key enforcement
            cursor = conn.cursor()

            # Create delivery_men table
            cursor.execute('''CREATE TABLE IF NOT EXISTS delivery_men (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                vehicle TEXT)''')

            # Create accounts table
            cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                email TEXT NOT NULL UNIQUE,
                                place TEXT,
                                password TEXT)''')

            # Create work_records table
            cursor.execute('''CREATE TABLE IF NOT EXISTS work_records (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                delivery_man_id INTEGER,
                                account_id INTEGER,
                                tips REAL,
                                orders_count INTEGER,
                                date TEXT,
                                shift_from TEXT,
                                shift_to TEXT,
                                confirmation_photo TEXT,
                                FOREIGN KEY (delivery_man_id) REFERENCES delivery_men(id)
                                    ON UPDATE CASCADE ON DELETE SET NULL,
                                FOREIGN KEY (account_id) REFERENCES accounts(id)
                                    ON UPDATE CASCADE ON DELETE SET NULL)''')

            # Commit the changes and close the connection
            conn.commit()
            print("Database and tables created successfully!")
        else:
            print("Database already exists. No action needed.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if 'conn' in locals() and conn:
            conn.close()