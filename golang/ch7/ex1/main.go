package main

import (
	"fmt"
	"log"
	"strings"
)

type ByteCounter int
type WordCounter int
type LineCounter int

func (c *ByteCounter) Write(p []byte) (int, error) {
	*c += ByteCounter(len(p))
	return len(p), nil
}

func (w *WordCounter) Write(p []byte) (int, error) {
	*w += WordCounter(len(strings.Split(string(p), " ")))
	return len(strings.Split(string(p), " ")), nil
}

func (l *LineCounter) Write(p []byte) (int, error) {
	*l += LineCounter(len(strings.Split(string(p), "\n")))
	return len(strings.Split(string(p), "\n")), nil
}

func main() {
	var (
		c ByteCounter
		w WordCounter
		l LineCounter
	)
	str := "hello neko\nneko"
	log.Println("Call Write method and Set value")
	fmt.Println("----\n" + str + "\n----")
	c.Write([]byte(str))
	w.Write([]byte(str))
	l.Write([]byte(str))
	fmt.Printf("c = %v\n", c)
	fmt.Printf("w = %v\n", w)
	fmt.Printf("l = %v\n", l)

	w, l, c = 0, 0, 0
	var name = "Dolly"
	fmt.Printf("hello,%s\n", name)
	fmt.Fprintf(&c, "hello,%s", name)
	fmt.Fprintf(&w, "hello,%s", name)
	fmt.Fprintf(&l, "hello,%s", name)
	fmt.Printf("c = %v\n", c)
	fmt.Printf("w = %v\n", w)
	fmt.Printf("l = %v\n", l)
}
