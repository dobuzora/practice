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

func bubbleSort(a [10000]int, n int) int {
	sw := 0
	flag := true
	for i := 0; flag; i++ {
		flag = false
		for j := n - 1; j >= i+1; j-- {
			if a[j] < a[j-1] {
				a[j], a[j-1] = a[j-1], a[j]
				flag = true
				sw++
			}
		}
	}
	return sw
}

func main() {
	var a [10000]int

	n := nextLine()

	for i, v := range splitElement() {
		a[i] = v
	}

	sw := bubbleSort(a, n)

	for i, v := range a {
		if i == n-1 {
			fmt.Println(v)
			break
		}
		fmt.Printf("%d ", v)
	}

	fmt.Println(sw)
}
