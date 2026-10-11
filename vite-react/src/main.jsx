import React from 'react'
import { createRoot } from 'react-dom/client'

function App() {
  return (
    <main style={{ fontFamily: 'system-ui', padding: 40, textAlign: 'center' }}>
      <h1>⚛️ vite-react @ MiniCloud</h1>
      <p>由 AI 產生的 multi-stage Dockerfile 建置：先 npm build，再以靜態伺服器監聽 8080。</p>
    </main>
  )
}

createRoot(document.getElementById('root')).render(<App />)
