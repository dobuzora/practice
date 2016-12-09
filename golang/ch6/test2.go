package main

import (
	"./prac"
	"fmt"
)

func main() {
	fmt.Println("Start!!")
	var x prac.IntSet
	x.Add(3)
	x.Add(6)
	x.AddAll(7, 8, 9)
	fmt.Println(x.String())
}
