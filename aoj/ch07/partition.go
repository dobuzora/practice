package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const MAX = 100000

var sc = bufio.NewScanner(os.Stdin)

func read() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}

func splitElements() []int {
	var list []int
	sc.Scan()
	if err := sc.Err(); err != nil {
		fmt.Printf("Scanner error: %q\n", err)
	}
	for _, v := range strings.Split(sc.Text(), " ") {
		num, _ := strconv.Atoi(v)
		list = append(list, num)
	}
	return list
}

func partition(A []int, p int, r int) int {
	x := A[r]
	i := p - 1
	for j := p; j < r; j++ {
		if A[j] <= x {
			i++
			A[i], A[j] = A[j], A[i]
		}
	}
	A[i+1], A[r] = A[r], A[i+1]
	return i + 1
}

func main() {
	var A []int
	// n := read()
	var n int
	fmt.Scan(&n)
	// A := splitElements()
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		//	fmt.Println(a, i)
		A = append(A, a)
	}

	q := partition(A, 0, n-1)

	for i, v := range A {
		if i != 0 {
			fmt.Print(" ")
		}
		if i == q {
			fmt.Print("[")
		}
		fmt.Print(v)
		if i == q {
			fmt.Print("]")
		}
	}
	fmt.Println()
}
