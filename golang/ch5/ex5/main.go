package main

import (
	"bufio"
	"fmt"
	"net/http"
	"regexp"
	"strings"

	"golang.org/x/net/html"
)

var content string
var imagecount int

// サーチ関数
func searchText(links []string, n *html.Node) []string {
	if n.Type == html.TextNode {
		content += fmt.Sprintf("%v ", n.Data)
	}

	for c := n.FirstChild; c != nil; c = c.NextSibling {
		if c.Data == "script" || c.Data == "style" {
			return links
		} else {
			if c.Data == "img" {
				imagecount++
			}
			links = searchText(links, c)
		}
	}
	return links
}

func countWordsAndImages(n *html.Node) (words, images int) {
	searchText(nil, n)

	rep := regexp.MustCompile(`\n`)
	str := rep.ReplaceAllString(content, "")

	input := bufio.NewScanner(strings.NewReader(str))
	input.Split(bufio.ScanWords)
	for input.Scan() {
		fmt.Println(input.Text())
		words++
	}
	return words, imagecount
}

func CountWordsAndImages(url string) (words, images int, err error) {
	resp, err := http.Get(url)
	if err != nil {
		return
	}
	doc, err := html.Parse(resp.Body)
	resp.Body.Close()
	if err != nil {
		return
	}
	words, images = countWordsAndImages(doc)
	return
}

func main() {
	url := "http://gigazine.net"
	w, i, _ := CountWordsAndImages(url)
	fmt.Println(w, i)
}
