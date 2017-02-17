package main

import "fmt"
import "./popcount1"
import "./popcount2"

func main() {
	var num uint64 = 255
	fmt.Println(popcount1.PopCount(num))
	fmt.Println(popcount2.PopCount(num))
}
