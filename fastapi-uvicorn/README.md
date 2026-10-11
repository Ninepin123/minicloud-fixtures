# fastapi-uvicorn

驗證目標：規則偵測到 python，但第一次會因為 `main.py` 寫死 `uvicorn.run(port=8000)` 而就緒逾時 →
**AI 修正**啟動指令為 `uvicorn main:app --host 0.0.0.0 --port $PORT` → 成功。

- `requirements.txt` 有 fastapi 與 uvicorn，但沒有 Procfile
- `main.py` 的 `uvicorn.run(app, port=8000)` 寫死了錯誤的埠
- 期望：建置成功 → 啟動逾時（沒有監聽 8080）→ repairing（AI 修正啟動指令）→ succeeded，repair_attempts ≥ 1

部署網址：`https://github.com/<帳號>/minicloud-fixtures/tree/main/fastapi-uvicorn`
