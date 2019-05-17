package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"./stack"
)

var sc = bufio.NewScanner(os.Stdin)

//splitElement return elements of one line.
func splitElement() []string {
	sc.Scan()
	return strings.Split(sc.Text(), " ")
}

func main() {
	var a, b int
	s := stack.New()

	for _, v := range splitElement() {
		if v == "+" {
			a = s.Pop()
			b = s.Pop()
			s.Push(a + b)
		} else if v == "-" {
			b = s.Pop()
			a = s.Pop()
			s.Push(a - b)
		} else if v == "*" {
			a = s.Pop()
			b = s.Pop()
			s.Push(a * b)
		} else {
			num, _ := strconv.Atoi(v)
			s.Push(num)
		}
	}

	fmt.Println(s.Pop())
}
