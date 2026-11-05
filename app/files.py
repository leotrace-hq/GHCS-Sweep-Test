import ipaddress
import os
import socket
from urllib.parse import urlsplit

import requests
from flask import Flask, Response, abort, request, send_file, send_from_directory

app = Flask(__name__)

UPLOAD_DIR = "/srv/uploads"

FETCH_ALLOWED_HOSTS = {h.strip().lower() for h in os.environ.get("FETCH_ALLOWED_HOSTS", "").split(",") if h.strip()}


def allowed_url(url):
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    if parts.scheme not in ("http", "https") or host not in FETCH_ALLOWED_HOSTS:
        return False
    try:
        infos = socket.getaddrinfo(host, parts.port or (443 if parts.scheme == "https" else 80))
    except socket.gaierror:
        return False
    return all(ipaddress.ip_address(info[4][0]).is_global for info in infos)


@app.route("/files/fetch")
def fetch():
    url = request.args.get("url", "")
    if not allowed_url(url):
        abort(400)
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
