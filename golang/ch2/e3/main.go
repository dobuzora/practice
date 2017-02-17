package main

import "fmt"
import "./popcount"

func main() {
	var num uint64 = 3
	fmt.Println(num)
	fmt.Println(popcount.PopCount(num))
}
