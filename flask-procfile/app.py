"""flask-procfile：規則偵測即成功的 Flask 範例（gunicorn 讀取 PORT）。"""
import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index() -> str:
    return "flask-procfile is running"


@app.get("/api/info")
def info() -> object:
    return jsonify({"app": os.environ.get("MC_APP", "?"),
                    "instance": os.environ.get("MC_INSTANCE_ID", "?")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
