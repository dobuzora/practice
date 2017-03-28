package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"

	"./github"
)

var now = strings.Split(time.Now().Format("2006-01-02"), "-")

func convertInt(s []string) []int {
	var nlist []int
	for _, n := range s {
		num, _ := strconv.Atoi(n)
		nlist = append(nlist, num)
	}
	return nlist
}

func checkDate(d string) int {
	date := strings.Split(d, "-")
	nlist := convertInt(now)
	dlist := convertInt(date)
	if nlist[0] > dlist[0]+1 { // 確実に一年以上か
		return 2
	} else if nlist[0] == dlist[0] { // 同いどし
		if nlist[1] == dlist[1] {
			return 0
		} else if nlist[1]-1 == dlist[1] {
			if nlist[2] > dlist[2] {
				return 1
			} else {
				return 0
			}

		} else {
			return 1
		}
	} else { // 一年以内の可能性あり
		if nlist[1] > dlist[1] { // 確実に一年以上
			return 2
		} else { // 一年以内か一ヶ月以内の可能性あり
			if nlist[1] == dlist[1] {
				return 0
			} else if nlist[1]-1 == dlist[1] {
				if nlist[2] > dlist[2] {
					return 1
				} else {
					return 0
				}
			} else {
				return 1
			}
		}
	}
}

func main() {
	result, err := github.SearchIssues(os.Args[1:])
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%d issues:\n", result.TotalCount)
	var withinOneMonth, withinOneYear, overYear []*github.Issue
	for _, item := range result.Items {
		switch checkDate(item.CreatedAt.Format("2006-01-02")) {
		case 0:
			withinOneMonth = append(withinOneMonth, item)
		case 1:
			withinOneYear = append(withinOneYear, item)
		case 2:
			overYear = append(overYear, item)
		}
	}

	var f = func(list []*github.Issue) {
		for _, item := range list {
			fmt.Printf("#%-5d %9.9s %.55s\n",
				item.Number, item.User.Login, item.CreatedAt.Format("2006-01-02"))
		}
	}

	fmt.Println("\t-- withinOneMonth --")
	f(withinOneMonth)
	fmt.Println("\t-- withinOneYear --")
	f(withinOneYear)
	fmt.Println("\t-- overYear --")
	f(overYear)

}
