# needs-db

驗證目標：Express 應用程式需要 `DATABASE_URL` → **AI 在 env 中宣告為 required** → 停在 `awaiting_input`。

- `server.js` 讀取 `process.env.DATABASE_URL`，缺少時拒絕啟動（退出）
- 期望：AI 規劃時宣告 DATABASE_URL 為必填 → 匯入停在 awaiting_input →
  e2e 腳本帶入假的 DATABASE_URL 後 approve → succeeded

部署網址：`https://github.com/<帳號>/minicloud-fixtures/tree/main/needs-db`
