# flask-procfile

驗證目標：**不呼叫 AI**，規則直接成功（驗證 assist 模式的規則優先路徑）。

- 有 `requirements.txt`（Python）與 `Procfile`（`web: gunicorn app:app`）
- gunicorn 會讀取環境變數 `PORT`，符合平台約定
- 期望：規則偵測為 python → 直接建置部署 → succeeded，AI 呼叫數 = 0

部署網址：`https://github.com/<帳號>/minicloud-fixtures/tree/main/flask-procfile`
