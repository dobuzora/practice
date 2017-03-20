package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

// echo1
func echo1() {
	var s, sep string
	for _, arg := range os.Args[1:] {
		s += sep + arg
		sep = " "
	}
	fmt.Println(s)
}

// echo2
func echo2() {
	fmt.Println(strings.Join(os.Args[1:], " "))
}

func main() {
	start := time.Now()
	echo1()
	fmt.Printf("\necho1: %f", time.Since(start).Seconds())

	fmt.Println("\n")

	start = time.Now()
	echo2()
	fmt.Printf("\necho2: %f", time.Since(start).Seconds())
}
