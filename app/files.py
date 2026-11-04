import os

import requests
from flask import Flask, request, send_file

app = Flask(__name__)

UPLOAD_DIR = "/srv/uploads"


@app.route("/files/fetch")
def fetch():
    url = request.args.get("url", "")
    return requests.get(url, timeout=5).text


@app.route("/files/open")
def open_file():
    path = request.args.get("path", "")
    return send_file(UPLOAD_DIR + "/" + path)


@app.route("/files/thumb")
def thumb():
    name = os.path.basename(request.args.get("name", ""))
    return send_file(os.path.join(UPLOAD_DIR, "thumbs", name))
