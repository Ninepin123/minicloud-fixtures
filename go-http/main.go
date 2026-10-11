// go-http：最小 Go HTTP 服務（讀取 PORT）。規則偵測不到 Go，測 AI 從零規劃。
package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "go-http is running on %s", port)
	})
	http.HandleFunc("/api/info", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, `{"app":"go-http","instance":"%s"}`, os.Getenv("MC_INSTANCE_ID"))
	})
	http.ListenAndServe(":"+port, nil)
}
