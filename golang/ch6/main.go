package main

import "./test"
import "fmt"

func main() {
	var x test.IntSet
	x.Add(4)
	x.Add(6)
	x.Add(124)
	x.Add(142)

	// Len()テスト
	fmt.Println(x.Len())
	fmt.Println(x.String())

	// Remove()テスト
	x.Remove(5)
	x.Remove(4)
	fmt.Println(x.String())

	// Copy()テスト
	y := x.Copy()

	// Clear()テスト
	x.Clear()
	fmt.Println(x.String())

	fmt.Println("y", y.String())

}
