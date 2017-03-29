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
	links := make(map[string]int)
	for k, v := range countItem(links, doc) {
		fmt.Printf("%9.9v : %v\n", k, v)
	}
}

func countItem(links map[string]int, n *html.Node) map[string]int {
	if n.Type == html.ElementNode {
		links[string(n.Data)]++
	}

	for c := n.FirstChild; c != nil; c = c.NextSibling {
		links = countItem(links, c)
	}
	return links
}
