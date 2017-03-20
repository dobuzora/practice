// URLの接頭辞http://がなければ追加するようしなさい
// strings.HasPrefixを使いたくなるかも...
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func main() {
	prefix := "http://"
	for _, url := range os.Args[1:] {
		if !strings.HasPrefix(url, prefix) {
			url = "http://" + url
		}
		resp, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch:%v", err)
			os.Exit(1)
		}
		b, err := ioutil.ReadAll(resp.Body)
		resp.Body.Close()
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: reading %s: %v", url, err)
			os.Exit(1)
		}
		fmt.Printf("%s", b)
	}
}
