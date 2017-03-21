package main

import (
	"bufio"
	"fmt"
)

func main() {
	neko := `hello world
	afdkaj
	afsdkljf
	asdfkj
	`
	inu := []byte(neko)
	fmt.Println(inu)
	ad, _, _ := bufio.ScanWords(inu, false)
	fmt.Println(ad)
}
