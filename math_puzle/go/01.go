package main

import (
	"fmt"
	"strconv"
)

func check10(num int) bool {
	str_num := strconv.Itoa(num)
	for i := range str_num {
		fmt.Println(i)
	}
	return true
}

func calc() {
	for i := 11; i < 20; i++ {
		if check10(i) {
			break
		}
	}
}

func main() {
	calc()
}
