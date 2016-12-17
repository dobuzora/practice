package main

import (
	"fmt"
	"io"
	"log"
	"net"
	"os"
	"runtime"
	"strings"
	"sync"
)

func main() {
	if len(os.Args) == 0 {
		fmt.Println("Fatal")
	} else {
		fmt.Println(runtime.NumCPU())
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
		var wg sync.WaitGroup
		wg.Add(3)
		go mustCopy(&wg, os.Stdout, connLists[0])
		go mustCopy(&wg, os.Stdout, connLists[1])
		go mustCopy(&wg, os.Stdout, connLists[2])
		wg.Wait()
		//mustCopy(os.Stdin, connLists[2])

		// メイン関数を終わらせないように
		//for {
		//}
	}

}

func mustCopy(wg *sync.WaitGroup, dst io.Writer, src io.Reader) {
	defer wg.Done()
	if _, err := io.Copy(dst, src); err != nil {
		log.Fatal(err)
	}
}
