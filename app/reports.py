import subprocess

from flask import Flask, request, send_from_directory

app = Flask(__name__)

REPORT_DIR = "/srv/reports"


@app.route("/reports/download")
def download():
    name = request.args.get("name", "")
    return send_from_directory(REPORT_DIR, name)


@app.route("/reports/archive")
def archive():
    target = request.args.get("target", "")
    out = subprocess.check_output(["tar", "czf", "/tmp/out.tgz", "--", target])
    return {"ok": True, "bytes": len(out)}
