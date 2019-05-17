package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func nextLine() int {
	sc.Scan()
	nums, _ := strconv.Atoi(sc.Text())
	return nums
}

func splitElement() []int {
	var nums []int
	sc.Scan()
	strs := strings.Split(sc.Text(), " ")
	for _, v := range strs {
		n, _ := strconv.Atoi(v)
		nums = append(nums, n)
	}
	return nums
}

func search(a [10001]int, n int, key int) bool {
	i := 0
	a[n] = key
	for a[i] != key {
		i++
	}
	return i != n
}

func main() {
	var a [10001]int
	var sum int
	n := nextLine()

	for i, v := range splitElement() {
		a[i] = v
	}

	nextLine()

	for _, v := range splitElement() {
		if search(a, n, v) {
			sum++
		}
	}

	fmt.Println(sum)
}
