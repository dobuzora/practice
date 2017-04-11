// メソッドを追加しなさい
package intset

import (
	"bytes"
	"fmt"
)

type IntSet struct {
	words []uint64
}

// Has reports whether the set contains the non-negative value x.
func (s *IntSet) Has(x int) bool {
	word, bit := x/64, uint(x%64)
	return word < len(s.words) && s.words[word]&(1<<bit) != 0
}

// Add adds the non-negative value x to the set.
func (s *IntSet) Add(x int) {
	word, bit := x/64, uint(x%64)
	for word >= len(s.words) {
		s.words = append(s.words, 0)
	}
	s.words[word] |= 1 << bit
}

// UnionWith sets s to the union of s and t.
func (s *IntSet) UnionWith(t *IntSet) {
	for i, tword := range t.words {
		if i < len(s.words) {
			s.words[i] |= tword
		} else {
			s.words = append(s.words, tword)
		}
	}
}

// String returns the set as a string of the form "{1 2 3}"
func (s *IntSet) String() string {
	var buf bytes.Buffer
	buf.WriteByte('{')
	for i, word := range s.words {
		if word == 0 {
			continue
		}
		for j := 0; j < 64; j++ {
			if word&(1<<uint(j)) != 0 {
				if buf.Len() > len("{") {
					buf.WriteByte(' ')
				}
				fmt.Fprintf(&buf, "%d", 64*i+j)
			}
		}
	}
	buf.WriteByte('}')
	return buf.String()
}

// 課題用追加メソッド
// 要素数を返します
func (s *IntSet) Len() int {
	var counter int
	for _, i := range s.words {
		for _, j := range fmt.Sprintf("%b", i) {
			if string(j) == "1" {
				counter++
			}
		}
	}
	return counter
}

// セットからxを取り除く
func (s *IntSet) Remove(x int) {
	word, bit := x/64, uint(x%64)
	if s.Has(x) {
		s.words[word] ^= 1 << bit
	}
}

// セットからすべての要素を取り除く
func (s *IntSet) Clear() {
	for i := 0; i < len(s.words); i++ {
		s.words[i] = 0
	}
}

// セットのコピーを返す
func (s *IntSet) Copy() *IntSet {
	var c IntSet
	for i := 0; i < len(s.words); i++ {
		c.words = append(c.words, s.words[i])
	}
	return &c
}
