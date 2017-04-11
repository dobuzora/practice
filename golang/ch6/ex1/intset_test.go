package intset

import "fmt"

func Example_one() {
	var x, y IntSet
	x.Add(1)
	x.Add(9)
	x.Add(13)
	fmt.Println(x.String()) // "{1 9 13}"

	y.Add(4)
	y.Add(9)
	fmt.Println(y.String()) // "{4 9}"

	x.UnionWith(&y)
	fmt.Println(x.String()) // {1 9 13 4}

	fmt.Println(x.Has(9), x.Has(2)) // true false

	fmt.Println(x.Len()) // 4

	x.Remove(9)
	fmt.Println(x.String()) // {1 4 13}

	z := x.Copy()
	fmt.Println(z.String()) // {1 4 13}

	x.Clear()
	fmt.Println(x.String()) // {}

	// Output:
	// {1 9 13}
	// {4 9}
	// {1 4 9 13}
	// true false
	// 4
	// {1 4 13}
	// {1 4 13}
	// {}
}
