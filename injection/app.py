"""injection：正常的 Flask 應用；README 內含 prompt injection 測試文字。"""
import os

from flask import Flask

app = Flask(__name__)


@app.get("/")
def index() -> str:
    return "injection-fixture is running (README 中的指示已被忽略)"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
