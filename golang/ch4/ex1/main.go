package main

import (
	"crypto/sha256"
	"fmt"
)

func CountDifferentBit(c1 [32]uint8, c2 [32]uint8) int {
	var count int
	c1list := ""
	for _, i := range c1 {
		c1list += fmt.Sprintf("%08b", i)
	}
	c2list := ""
	for _, i := range c2 {
		c2list += fmt.Sprintf("%08b", i)
	}
	for i, n := range c1list {
		if uint8(n) != c2list[i] {
			count++
		}
	}
	return count
}

func main() {
	c1 := sha256.Sum256([]byte("x"))
	c2 := sha256.Sum256([]byte("X"))
	count := CountDifferentBit(c1, c2)
	fmt.Printf("different bit count : %d\n", count)
}
