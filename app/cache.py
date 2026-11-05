import hashlib

from flask import Flask, request

app = Flask(__name__)
_cache = {}


def cache_key(path, query):
    return hashlib.md5((path + "?" + query).encode()).hexdigest()


@app.route("/cached")
def cached():
    key = cache_key(request.path, request.query_string.decode())
    return {"hit": key in _cache}


if __name__ == "__main__":
    app.run()
