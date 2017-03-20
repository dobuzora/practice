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
		for filename, counts := range fcounts {
			for lines, n := range counts {
				if n > 1 {
					fmt.Printf("%s %d %s\n", filename, n, lines)
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
	for input.Scan() {
		counts[input.Text()]++
		if fcounts != nil {
			fcounts[f.Name()] = counts
		}
	}
}
