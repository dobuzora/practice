// ここのインデックスと値の組みを一行ごとに表示しなさい
package main

import (
	"fmt"
	"os"
)

func main() {
	for i, args := range os.Args[1:] {
		fmt.Println(i, args)
	}
}
