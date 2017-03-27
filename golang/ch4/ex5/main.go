package main

import "fmt"

func OverlapRemove(s []string) []string {
	var rindex []int
	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+1] {
			rindex = append(rindex, i)
		}
	}
	var re []string
	for i, n := range rindex {
		re = s[n-i+1:]
		s = append(s[:n-i], re...)
		//s = append(s[:i+n], s[:n-1])
	}
	return s
}

func main() {
	test1 := []string{"n", "e", "e", "k", "o", "n", "n", "o"}
	fmt.Println(test1)
	fmt.Println(OverlapRemove(test1))
}
