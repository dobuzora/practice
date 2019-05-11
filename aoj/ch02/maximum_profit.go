package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

const MAX int = 200000

// Max returns the larger of x or y.
func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

// Min returns the smaller of x or y.
func Min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

// read next line.
func nextLine() int {
	sc.Scan()
	out, _ := strconv.Atoi(sc.Text())
	return out
}

func main() {
	var R [MAX]int
	n := nextLine()
	for i := 0; i < n; i++ {
		R[i] = nextLine()
	}

	maxv := -2000000000
	minv := R[0]

	for _, v := range R {
		maxv = Max(maxv, v-minv)
		minv = Min(minv, v)
	}

	fmt.Println(maxv)

}
