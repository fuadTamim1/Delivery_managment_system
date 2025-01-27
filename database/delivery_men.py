from .connection import get_connection
from tkinter import messagebox


def all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, vehicle FROM delivery_men")
    result = cursor.fetchall()
    conn.close()
    return result


def get(delivery_man_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, vehicle FROM delivery_men WHERE id = ?", (delivery_man_id,)
    )
    result = cursor.fetchone()
    conn.close()
    return result

def nameOf(id):
    """Return all the data from the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM delivery_men WHERE id = ?", (id,))
    response = cur.fetchone()
    conn.close()
    return response[0]

def create(name, vehicle):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO delivery_men (name, vehicle) VALUES (?, ?)",
        (
            name,
            vehicle,
        ),
    )
    conn.commit()
    conn.close()
    return True


def get_delivery_men():
    """Fetch delivery men names for dropdown selection."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM delivery_men")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]


def get_delivery_men_ids():
    """Fetch delivery men names for dropdown selection."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM delivery_men")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]


def update(name, vehicle, delivery_man_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE delivery_men
        SET name = ?, vehicle = ? 
        WHERE id = ?
    """,
        (name, vehicle, delivery_man_id),
    )
    conn.commit()
    conn.close()


def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM delivery_men WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def filter_delivery_men(user_search, start_date=None, end_date=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT id, name, vehicle
        FROM delivery_men 
        WHERE name LIKE ?
    """

    parameters = [f"%{user_search}%"]

    if start_date and end_date:
        query += " AND (date_column BETWEEN ? AND ?)"
        parameters.extend([start_date, end_date])

    cursor.execute(query, parameters)
    result = cursor.fetchall()
    conn.close()
    return result
