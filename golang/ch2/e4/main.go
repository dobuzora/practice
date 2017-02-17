package main

import "fmt"
import "./popcount1"
import "./popcount2"

func main() {
	var num uint64 = 7
	for i := 0; i < 64; i++ {
		fmt.Println(num >> uint64(i) & 1)
	}
	fmt.Println(popcount1.PopCount(num))
	fmt.Println(popcount2.PopCount(num))
}
