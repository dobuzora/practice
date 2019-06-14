package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func read() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}

func splitElements() []int {
	var list []int
	sc.Scan()
	for _, v := range strings.Split(sc.Text(), " ") {
		num, _ := strconv.Atoi(v)
		list = append(list, num)
	}
	return list
}

var cnt int

func merge(A []int, n int, left int, mid int, right int) {
	n1 := mid - left
	n2 := right - mid
	var L, R []int
	for i := 0; i < n1; i++ {
		//L[i] = A[left+i]
		L = append(L, A[left+i])
	}
	for i := 0; i < n2; i++ {
		// R[i] = A[mid+i]
		R = append(R, A[mid+i])
	}
	L = append(L, 200000)
	R = append(R, 200000)
	i, j := 0, 0
	for k := left; k < right; k++ {
		cnt++
		if L[i] <= R[j] {
			A[k] = L[i]
			i++
		} else {
			A[k] = R[j]
			j++
		}
	}
}

func mergeSort(A []int, n int, left int, right int) {
	if left+1 < right {
		mid := (left + right) / 2
		// fmt.Println(left, mid, right)
		mergeSort(A, n, left, mid)
		mergeSort(A, n, mid, right)
		merge(A, n, left, mid, right)
	}
}

func main() {
	n := read()
	A := splitElements()

	mergeSort(A, n, 0, n)

	for i, v := range A {
		if i == n-1 {
			fmt.Println(v)
			break
		}
		fmt.Print(v, " ")
	}
	fmt.Println(cnt)

}
