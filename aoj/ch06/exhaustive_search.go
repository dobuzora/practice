package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func read() string {
	sc.Scan()
	return sc.Text()
}

//splitElement return elements of one line.
func splitElement() []int {
	var list []int
	sc.Scan()
	for _, v := range strings.Split(sc.Text(), " ") {
		num, _ := strconv.Atoi(v)
		list = append(list, num)
	}
	return list
}

func solve(i int, m int) bool {
	if m == 0 {
		return true
	}
	if i >= n {
		return false
	}
	res := solve(i+1, m) || solve(i+1, m-A[i])
	return res
}

var A []int
var n int

func main() {
	n, _ = strconv.Atoi(read())
	A = splitElement()
	read()
	for _, q := range splitElement() {
		if solve(0, q) {
			fmt.Println("yes")
		} else {
			fmt.Println("no")
		}
	}
}
