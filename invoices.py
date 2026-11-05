import sqlite3


def invoices_for(db_path, customer):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, amount FROM invoices WHERE customer = ?", (customer,))
    return cur.fetchall()
