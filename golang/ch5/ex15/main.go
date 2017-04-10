package main

import (
	"fmt"
	"os"
)

func max(vals ...int) int {
	if len(vals) == 0 {
		fmt.Println("error:")
		os.Exit(1)
	}
	var max int
	for _, v := range vals {
		if max < v {
			max = v
		}
	}
	return max
}

func min(vals ...int) int {
	if len(vals) == 0 {
		fmt.Println("error:")
		os.Exit(1)
	}
	min := vals[0]
	for _, v := range vals {
		if min > v {
			min = v
		}
	}
	return min
}

func main() {
	values := []int{1, 5, 3, 6, 4, 7, 8, 0}
	fmt.Println(max(values...))
	fmt.Println(min(values...))
	fmt.Println(max())
	//fmt.Println(min())
	//fmt.Println(nmax())
	//fmt.Println(nmin())
}
