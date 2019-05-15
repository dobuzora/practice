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

// selectionSort retrun sw count.
func selectionSort(a [10000]int, n int) int {
	sw := 0
	for i := 0; i < n-1; i++ {
		minj := i
		for j := i; j < n; j++ {
			if a[j] < a[minj] {
				minj = j
			}
		}
		a[i], a[minj] = a[minj], a[i]
		if i != minj {
			sw++
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

	sw := selectionSort(a, n)

	for i, v := range a {
		if i == n-1 {
			fmt.Println(v)
			break
		}
		fmt.Printf("%d ", v)
	}
	fmt.Println(sw)
}
