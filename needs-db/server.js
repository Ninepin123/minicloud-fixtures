// needs-db：需要 DATABASE_URL 才啟動的 Express 應用（測 awaiting_input）。
const express = require('express')

const DATABASE_URL = process.env.DATABASE_URL
if (!DATABASE_URL) {
  console.error('缺少必要的環境變數 DATABASE_URL，拒絕啟動')
  process.exit(1)
}

const app = express()
const port = process.env.PORT || 8080

app.get('/', (req, res) => {
  res.json({ app: 'needs-db', db: DATABASE_URL.slice(0, 20) + '…' })
})

app.listen(port, '0.0.0.0', () => {
  console.log(`needs-db listening on ${port}`)
})
