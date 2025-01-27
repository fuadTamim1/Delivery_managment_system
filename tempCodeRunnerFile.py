
    # def update_work_records_table(self):
    #     """Fetch delivery men data from the database and update the table."""
    #     conn = sqlite3.connect(self.db_path)
    #     cursor = conn.cursor()

    #     # Query all delivery men data from the database
    #     cursor.execute("SELECT name, email, vehicle, age FROM delivery_men")
    #     rows = cursor.fetchall()

    #     # Clear any existing rows in the Treeview
    #     for row in self.delivery_men_table.get_children():
    #         self.delivery_men_table.delete(row)

    #     # Insert new rows into the Treeview
    #     for row in rows:
    #         self.delivery_men_table.insert("", "end", values=row)
    #         print('array', row)
    #     conn.close()
