package main

import "fmt"

type ByteCounter int
type WordCOunter int
type LineCounter int

func (c *ByteCounter) Write(p []byte) (int, error) {
	*c += ByteCounter(len(p))
	return len(p), nil
}

func (w *WordCounter) Write(p []byte) (int, error) {

}

func (w *LineCounter) Write(p []byte) (int, error) {
}

func main() {
	var c ByteCounter
	c.Write([]byte("hello"))
	fmt.Println(c)

	c = 0
	var name = "Dolly"
	fmt.Fprintf(&c, "hello,%s", name)
	fmt.Println(c)
}
