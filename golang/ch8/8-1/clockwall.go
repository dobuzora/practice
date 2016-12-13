package main

import (
	"fmt"
	"io"
	"log"
	"net"
	"os"
	"strings"
)

func main() {
	if len(os.Args) == 0 {
		fmt.Println("Fatal")
	} else {
		var connLists []net.Conn
		for _, str := range os.Args[1:] {
			addr := strings.Split(str, "=")
			conn, err := net.Dial("tcp", addr[1])
			if err != nil {
				log.Fatal(err)
			}
			fmt.Println(conn)
			connLists = append(connLists, conn)
		}
		go mustCopy(os.Stdout, connLists[0])
		go mustCopy(os.Stdout, connLists[1])
		go mustCopy(os.Stdout, connLists[2])
		// メイン関数を終わらせないように
		for {
		}
	}

}

func mustCopy(dst io.Writer, src io.Reader) {
	if _, err := io.Copy(dst, src); err != nil {
		log.Fatal(err)
	}
}
