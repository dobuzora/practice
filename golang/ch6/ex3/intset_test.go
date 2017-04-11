package intset

import "fmt"

func Example_one() {
	var x, y IntSet
	x.Add(2)
	x.Add(4)
	x.Add(6)
	y.Add(1)
	y.Add(3)
	y.Add(6)
	x.IntersectWith(&y)
	fmt.Println(x.String()) // {6}

	var i, j IntSet
	i.Add(1)
	i.Add(2)
	i.Add(3)
	j.Add(2)
	j.Add(3)
	j.Add(4)
	i.DifferenceWith(&j)
	fmt.Println(i.String()) // {1}

	var a, b IntSet
	a.Add(1)
	a.Add(2)
	a.Add(3)
	b.Add(2)
	b.Add(3)
	b.Add(4)

	a.SymmetricDifference(&b)
	fmt.Println(a.String()) // {1 4}

	// Output:
	// {6}
	// {1}
	// {1 4}
}
