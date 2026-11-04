from flask import Flask, redirect, request

app = Flask(__name__)

SAFE_DESTINATIONS = {"home": "/", "orders": "/orders", "reports": "/reports/download"}


@app.route("/profile/greet")
def greet():
    name = request.args.get("name", "")
    return "<h1>Hello " + name + "</h1>"


@app.route("/profile/leave")
def leave():
    target = request.args.get("next", "/")
    return redirect(target)


@app.route("/profile/go")
def go():
    return redirect(SAFE_DESTINATIONS.get(request.args.get("to", "home"), "/"))
