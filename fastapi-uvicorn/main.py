"""fastapi-uvicorn：故意寫死 port=8000 的 FastAPI 範例（測 AI 自動修正）。"""
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> dict:
    return {"app": "fastapi-uvicorn", "instance": os.environ.get("MC_INSTANCE_ID", "?")}


if __name__ == "__main__":
    # 故意寫死 8000：平台要求監聽 PORT（8080），第一次啟動會就緒逾時
    uvicorn.run(app, host="0.0.0.0", port=8000)
