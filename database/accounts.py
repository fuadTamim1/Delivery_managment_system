from .connection import get_connection


def all():
    """Return all the data from the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, email, place FROM accounts")
    response = cur.fetchall()
    conn.close()
    return response


def get(account_id):
    """Return all the data from the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT email,password, place FROM accounts where id = ?", (account_id,)
    )
    response = cur.fetchone()
    conn.close()
    return response


def get_emails():
    """Return all the data from the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT email FROM accounts")
    response = cur.fetchall()
    conn.close()
    return [row[0] for row in response]


def emailOf(id):
    """Return all the data from the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT email FROM accounts WHERE id = ?", (id,))
    response = cur.fetchone()
    conn.close()
    return response[0]


def get_accounts_ids():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM accounts")
    response = cur.fetchall()
    conn.close()
    return [row[0] for row in response]


def create(email, password, place=""):
    """Create a new user in the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO accounts (email, password, place) VALUES (?, ?, ?)",
        (email, password, place),
    )
    conn.commit()
    conn.close()


def update(email, password, place, account_id):
    """Update account details for a specific account."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """UPDATE accounts SET email = ?, password = ?, place = ? WHERE id = ?""",
        (email, password, place, account_id),
    )
    conn.commit()
    conn.close()


def filter_accounts(user_search, start_date=None, end_date=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT id, email, place
        FROM accounts
        WHERE email LIKE ?
    """

    parameters = [f"%{user_search}%"]

    if start_date and end_date:
        query += " AND (date_column BETWEEN ? AND ?)"
        parameters.extend([start_date, end_date])

    cursor.execute(query, parameters)
    result = cursor.fetchall()
    conn.close()
    return result


def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE id = ?", (id,))
    conn.commit()
    conn.close()