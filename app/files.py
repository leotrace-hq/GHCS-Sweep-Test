import os

import requests
from flask import Flask, Response, abort, request, send_file, send_from_directory

app = Flask(__name__)

UPLOAD_DIR = "/srv/uploads"

FETCH_SOURCES = {
    "status": "https://www.githubstatus.com/api/v2/status.json",
}


@app.route("/files/fetch")
def fetch():
    url = FETCH_SOURCES.get(request.args.get("source", ""))
    if url is None:
        abort(404)
    body = requests.get(url, timeout=5, allow_redirects=False).text
    return Response(body, mimetype="text/plain", headers={"X-Content-Type-Options": "nosniff"})


@app.route("/files/open")
def open_file():
    path = request.args.get("path", "")
    return send_from_directory(UPLOAD_DIR, path)


@app.route("/files/thumb")
def thumb():
    name = os.path.basename(request.args.get("name", ""))
    return send_file(os.path.join(UPLOAD_DIR, "thumbs", name))
