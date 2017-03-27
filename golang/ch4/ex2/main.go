package main

import (
	"crypto/sha256"
	"crypto/sha512"
	"flag"
	"fmt"
)

func main() {
	var shaVer = flag.String("s", "sha256", "Type of sha to use")
	flag.Parse()

	input := flag.Args()

	switch *shaVer {
	case "sha256":
		fmt.Printf("%x\n", sha256.Sum256([]byte(input[0])))
	case "sha384":
		fmt.Printf("%x\n", sha512.Sum384([]byte(input[0])))
	case "sha512":
		fmt.Printf("%x\n", sha512.Sum512([]byte(input[0])))
	default:
		fmt.Printf("Unknown sha type : %s", *shaVer)
		return
	}
}
