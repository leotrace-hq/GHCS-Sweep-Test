import os
import subprocess

from flask import Flask, request, send_file

app = Flask(__name__)

REPORT_DIR = "/srv/reports"


@app.route("/reports/download")
def download():
    name = request.args.get("name", "")
    return send_file(os.path.join(REPORT_DIR, name))


@app.route("/reports/archive")
def archive():
    target = request.args.get("target", "")
    out = subprocess.check_output("tar czf /tmp/out.tgz " + target, shell=True)
    return {"ok": True, "bytes": len(out)}
