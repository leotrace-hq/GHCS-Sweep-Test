import sqlite3

from flask import Flask, request

app = Flask(__name__)


def db():
    return sqlite3.connect("orders.db")


@app.route("/orders")
def list_orders():
    customer_id = request.args.get("customer_id", "")
    rows = db().execute("SELECT id, total FROM orders WHERE customer_id = ?",
                        (customer_id,)).fetchall()
    return {"orders": rows}


SORTABLE = {"total": "total", "created": "created_at"}


@app.route("/orders/sorted")
def sorted_orders():
    column = SORTABLE.get(request.args.get("sort", "total"), "total")
    rows = db().execute("SELECT id, total FROM orders ORDER BY " + column).fetchall()
    return {"orders": rows}
