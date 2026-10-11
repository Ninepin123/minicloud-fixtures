# go-http

驗證目標：規則偵測**失敗**（只有 go.mod 和 main.go，不支援 Go）→ **AI 從零規劃** multi-stage Go Dockerfile → 成功。

- `main.go` 正確讀取 `PORT` 環境變數（AI 產生的 Dockerfile 只需要正確編譯執行）
- 期望：analyzing 時規則失敗 → AI 規劃（purpose=plan，stack 大約是 go/net-http）→ succeeded，ai_calls ≥ 1

部署網址：`https://github.com/<帳號>/minicloud-fixtures/tree/main/go-http`
