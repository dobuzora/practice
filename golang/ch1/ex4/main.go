package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	//counts := make(map[string]int)
	fcounts := make(map[string]map[string]int)
	counts := map[string]int{}
	files := os.Args[1:]
	if len(files) == 0 {
		fcounts = nil
		countLines(os.Stdin, counts, fcounts)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprint(os.Stderr, "dup2: %v\n", err)
				continue
			}
			countLines(f, counts, fcounts)
			f.Close()
		}
	}
	if fcounts != nil {
		fmt.Println(fcounts["test/fruit1"])
		fmt.Println(fcounts["test/fruit2"])
		fmt.Println(fcounts["test/fruit3"])
		fmt.Println("\n------------------------\n")
		for k, v := range counts {
			if v > 1 {
				fmt.Printf("%s : %d\n", k, v)
				for file, _ := range fcounts {
					for i, _ := range fcounts[file] {
						if k == i {
							fmt.Println(file)
						}
					}
				}
			}
		}

	} else {
		for lines, n := range counts {
			if n > 1 {
				fmt.Printf("%d\t%s\n", n, lines)
			}
		}
	}

}

func countLines(f *os.File, counts map[string]int, fcounts map[string]map[string]int) {
	input := bufio.NewScanner(f)
	ele := make(map[string]int)
	for input.Scan() {
		s := input.Text()
		counts[s]++
		ele[s]++
	}
	fcounts[f.Name()] = ele
}
