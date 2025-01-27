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
    cur.execute("SELECT id, email, place FROM accounts where id = ?", (account_id,))
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
