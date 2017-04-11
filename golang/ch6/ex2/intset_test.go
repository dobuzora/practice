package intset

import "fmt"

func Example_one() {
	var x IntSet
	x.Add(3)
	fmt.Println(x.String()) // {3}

	x.AddAll(5, 1, 7, 8)
	fmt.Println(x.String()) // {1 3 5 7 8}

	// :Output
	// {3}
	// {1 3 5 7 8}
}
