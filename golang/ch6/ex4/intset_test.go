package intset

import "fmt"

func Example_one() {
	var x IntSet
	x.Add(2)
	x.Add(5)
	x.Add(1)
	fmt.Println(x.Elems())

	// Output:
	// [1 2 5]
}
