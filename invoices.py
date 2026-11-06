import sqlite3


def invoices_for(db_path, customer, limit=50):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, amount FROM invoices WHERE customer = ? LIMIT ?", (customer, int(limit)))
    return cur.fetchall()
