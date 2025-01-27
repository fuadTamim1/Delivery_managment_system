from database.connection import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("DELETE FROM work_records where id < 4")
conn.commit()
conn.close()