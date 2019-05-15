package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

// nextLine is to read next line.
func nextLine() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}

// splitElement return elements of one line.
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

// trace print Array content.
func trace(a [1000000]int, n int) {
	for i := 0; i < n; i++ {
		if i != 0 {
			fmt.Print(" ")
		}
		fmt.Printf("%d", a[i])
	}
	fmt.Println()
}

func insertionSort(a [1000000]int, n int) {
	for i := 0; i < n; i++ {
		v := a[i]
		j := i - 1
		for j >= 0 && a[j] > v {
			a[j+1] = a[j]
			j--
		}
		a[j+1] = v
		// trace(a, n)
	}
}

func main() {
	var a [1000000]int

	n := nextLine()
	for i, v := range splitElement() {
		a[i] = v
	}

	insertionSort(a, n)
}
