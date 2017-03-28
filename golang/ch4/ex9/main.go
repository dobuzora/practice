package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Printf("error : %v", err)
		os.Exit(1)
	}
	defer file.Close()

	wcounter := make(map[string]int)

	input := bufio.NewScanner(file)
	input.Split(bufio.ScanWords)
	for input.Scan() {
		wcounter[fmt.Sprintf("%s", input.Text())]++
	}
	for k, v := range wcounter {
		fmt.Printf("%v : %d\n", k, v)
	}
}
