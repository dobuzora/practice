// 凡庸変換プログラム
package main

import (
	"fmt"
	"os"
	"strconv"

	"../e1"
)

func main() {
	for _, arg := range os.Args[1:] {
		t, err := strconv.ParseFloat(arg, 64)
		if err != nil {
			fmt.Fprintf(os.Stderr, "main: %v\n", err)
			os.Exit(1)
		}
		f := e1.Fahrenheit(t)
		c := e1.Celsius(t)
		k := e1.Kelvin(t)
		fmt.Printf("%s = %s,%s = %s,%s = %s\n", f, e1.FtoC(f), c, e1.CtoF(c), k, e1.KtoC(k))
	}
}
