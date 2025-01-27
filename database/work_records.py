from .connection import get_connection


def all():
    conn = get_connection()
    cursor = conn.cursor()

    # Query all work records data from the database
    cursor.execute(
        """
        SELECT id, delivery_man_id, account_id, orders_count, tips, date, 
            shift_from || ' - ' || shift_to AS shift, confirmation_photo 
        FROM work_records
    """
    )
    result = cursor.fetchall()
    conn.close()
    return result


def get_records_with_delivery_name():
    conn = get_connection()
    cursor = conn.cursor()

    # Query all work records data from the database, including delivery man's name
    cursor.execute(
        """
        SELECT wr.id, dm.name AS delivery_man_name, ac.email AS account, wr.orders_count, wr.tips, wr.date, 
               wr.shift_from || ' - ' || wr.shift_to AS shift, wr.confirmation_photo 
        FROM work_records wr
        JOIN delivery_men dm ON wr.delivery_man_id = dm.id
        JOIN accounts ac ON wr.account_id = ac.id
    """
    )
    result = cursor.fetchall()
    conn.close()
    return result


def get(work_record_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT delivery_man_id, account_id, orders_count, tips, date, shift_from, shift_to, confirmation_photo FROM work_records WHERE id = ?",
        (work_record_id,),
    )
    result = cursor.fetchone()
    conn.close()
    return result


def create(
    delivery_man,
    account,
    tips,
    orders_count,
    date,
    shift_from,
    shift_to,
    confirmation_photo,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO work_records (delivery_man_id,account_id, tips, orders_count, date, shift_from, shift_to, confirmation_photo) VALUES (?,?,?,?,?,?,?,?);",
        (
            delivery_man,
            account,
            tips,
            orders_count,
            date,
            shift_from,
            shift_to,
            confirmation_photo,
        ),
    )
    conn.commit()
    conn.close()


def update(
    delivery_man_id,
    account_id,
    tips,
    orders_count,
    date,
    shift_from,
    shift_to,
    confirmation_photo,
    work_record_id,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE work_records
        SET delivery_man_id = ?, account_id = ?, tips = ?, orders_count = ?, date = ?, shift_from = ?, shift_to = ?, confirmation_photo = ?
        WHERE id = ? """,
        (
            delivery_man_id,
            account_id,
            tips,
            orders_count,
            date,
            shift_from,
            shift_to,
            confirmation_photo,
            work_record_id,
        ),
    )

    conn.commit()
    conn.close()


def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM work_records WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def filter_work_records(user_search, start_date=None, end_date=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT wr.id, dm.name AS delivery_man_name, ac.email AS account, wr.tips, wr.orders_count, wr.date, 
               wr.shift_from || ' - ' || wr.shift_to AS shift, wr.confirmation_photo 
        FROM work_records wr
        JOIN delivery_men dm ON wr.delivery_man_id = dm.id
        JOIN accounts ac ON wr.account_id = ac.id
        WHERE dm.name LIKE ?
    """

    parameters = [f"%{user_search}%"]

    if start_date and end_date:
        query += " AND (date BETWEEN ? AND ?)"
        parameters.extend([start_date, end_date])

    cursor.execute(query, parameters)
    result = cursor.fetchall()
    conn.close()
    return result

def get_data_to_export():
    conn = get_connection()
    cursor = conn.cursor()

    # Query all work records data from the database
    cursor.execute(
        """
        SELECT id, delivery_man_id, account_id, orders_count, tips, date, 
            shift_from || ' - ' || shift_to AS shift
        FROM work_records
    """
    )
    result = cursor.fetchall()
    conn.close()
    return result