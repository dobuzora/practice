package main

import (
	"fmt"
	"io"
	"log"
	"os"

	"golang.org/x/net/html"
)

type Reader struct {
	s string
}

func (r *Reader) Read(b []byte) (n int, err error) {
	n = copy(b, r.s)
	return 0, io.EOF
}

func NewReader(s string) io.Reader { return &Reader{s} }

func main() {
	s := `<html>
  <head>
    <title> Title </title>
  </head>
  <body>
  Body
  </body>
</html>`
	fmt.Println(s)
	r := NewReader(s)
	doc, err := html.Parse(r)
	if err != nil {
		log.Fatal(os.Stdin, "error :%v", err)
	}
	fmt.Println(doc)
}
