import sqlite3


def orders_for(db_path, customer):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, total FROM orders WHERE customer = ?", (customer,))
    return cur.fetchall()
