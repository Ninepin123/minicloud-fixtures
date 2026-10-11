# minicloud-fixtures

MiniCloud「AI 輔助 GitHub 一鍵部署」的測試 repo（見 `docs/spec/12-github-import.md` 第 15 節）。

把這個資料夾推到自己的 GitHub（例如 `<帳號>/minicloud-fixtures`），再執行：

```powershell
.\.venv\Scripts\python scripts\e2e_import.py --repo https://github.com/<帳號>/minicloud-fixtures
```

| 子目錄 | 驗證重點 | 期望結果 |
|---|---|---|
| `flask-procfile/` | 規則優先（assist） | 不呼叫 AI，直接成功 |
| `fastapi-uvicorn/` | AI 自動修正 | 寫死 port=8000 → 逾時 → AI 改啟動指令 → 成功 |
| `go-http/` | AI 從零規劃 | 規則不支援 Go → multi-stage Dockerfile → 成功 |
| `vite-react/` | 前端建置策略 | build 階段＋靜態伺服器 → 成功 |
| `needs-db/` | 必填環境變數 | 宣告 DATABASE_URL → 停在 awaiting_input |
| `injection/` | prompt injection 防護 | README 的惡意指示被忽略（或被 validator 攔下） |
