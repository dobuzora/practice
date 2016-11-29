package main

import (
	"crypto/rand"
	"encoding/binary"
	"fmt"
	"strconv"
)

func main() {
	for i := 0; i < 100; i++ {
		fmt.Print(random(), " ")
	}
	fmt.Println()
}

func random() string {
	var n uint64
	binary.Read(rand.Reader, binary.LittleEndian, &n)
	return strconv.FormatUint(n, 36)
}
