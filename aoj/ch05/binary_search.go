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

func binarySearch(a [100000]int, n int, key int) bool {
	left := 0
	right := n
	var mid int
	for left < right {
		mid = (left + right) / 2
		if key == a[mid] {
			return true
		}
		if key > a[mid] {
			left = mid + 1
		} else if key < a[mid] {
			right = mid
		}
	}
	return false
}

func main() {
	var a [100000]int
	var sum int
	n := nextLine()

	for i, v := range splitElement() {
		a[i] = v
	}

	nextLine()

	for _, v := range splitElement() {
		if binarySearch(a, n, v) {
			sum++
		}
	}

	fmt.Println(sum)
}
