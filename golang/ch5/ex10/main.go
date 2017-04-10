package main

import "fmt"

var prereqs = map[string][]string{
	"algorithms": {"data structures"},
	"calculus":   {"linear algebra"},

	"compilers": {
		"data structures",
		"formal languages",
		"computer organization",
	},

	"data structures":       {"discrete math"},
	"databases":             {"data structures"},
	"discrete math":         {"intro to programming"},
	"formal languages":      {"discrete math"},
	"networks":              {"operating systems"},
	"operating systems":     {"data structures", "computer organization"},
	"programming languages": {"data structures", "computer organization"},
}

func main() {
	for i, course := range topoSort(prereqs) {
		fmt.Printf("%d:\t%s\n", i+1, course)
	}
}

func topoSort(m map[string][]string) []string {
	var order []string
	seen := make(map[string]bool)
	var visitAll func(items map[string]int)

	visitAll = func(items map[string]int) {
		for item, _ := range items {
			if !seen[item] {
				seen[item] = true
				next := make(map[string]int)
				for _, i := range m[item] {
					next[i] = 0
				}
				visitAll(next)
				order = append(order, item)
			}
		}
	}

	keys := make(map[string]int)
	for key := range m {
		keys[key] = 0
	}

	visitAll(keys)
	return order
}
