import os

import requests
from flask import Flask, request, send_file, send_from_directory

app = Flask(__name__)

UPLOAD_DIR = "/srv/uploads"


@app.route("/files/fetch")
def fetch():
    url = request.args.get("url", "")
    return requests.get(url, timeout=5).text


@app.route("/files/open")
def open_file():
    path = request.args.get("path", "")
    return send_from_directory(UPLOAD_DIR, path)


@app.route("/files/thumb")
def thumb():
    name = os.path.basename(request.args.get("name", ""))
    return send_file(os.path.join(UPLOAD_DIR, "thumbs", name))
