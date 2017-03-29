package main

import (
	"fmt"
	"os"

	"golang.org/x/net/html"
)

func main() {
	doc, err := html.Parse(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "findlinks1: %v\n", err)
		os.Exit(1)
	}
	printText(nil, doc)
}

func printText(links []string, n *html.Node) []string {
	// テキストノードであれば表示
	if n.Type == html.TextNode {
		fmt.Println(n.Data)
	}

	for c := n.FirstChild; c != nil; c = c.NextSibling {
		// フィルターをかける
		if c.Data == "script" || c.Data == "style" {
			return links
		} else {
			links = printText(links, c)
		}
	}
	return links
}
