package main

import (
	"fmt"
	"io"
)

type ByteCounter int

type countingWriter struct {
	count  *int64
	writer io.Writer
}

func (c *ByteCounter) Write(p []byte) (int, error) {
	*c += ByteCounter(len(p))
	return len(p), nil
}

func (c countingWriter) Write(p []byte) (int, error) {
	n, err := c.writer.Write(p)
	if err == nil {
		*c.count += int64(n)
	}
	return n, err
}

func CountingWriter(w io.Writer) (io.Writer, *int64) {
	var c int64
	retval := countingWriter{&c, w}
	return retval, retval.count
}

func main() {
	var c ByteCounter
	str := "Get on your knees! Beg for your life!"
	fmt.Fprintf(&c, "%v", str)
	fmt.Printf("c = %v\n", c)
	cw, b := CountingWriter(&c)
	fmt.Fprintf(cw, "%v", str)
	fmt.Println("==== Next Step =====")
	fmt.Printf("c = %v\n", c)
	fmt.Printf("b = %v\n", *b)
}
