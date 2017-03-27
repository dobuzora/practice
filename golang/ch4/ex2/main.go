package main

import (
	"flag"
	"fmt"
)

func main() {
	var shaVer = flag.String("s", "sha256", "Type of sha to use")
	flag.Parse()

	fmt.Println(*shaVer)

}
