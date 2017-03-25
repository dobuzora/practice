package main

import (
	"strings"
	"testing"
)

func TestCharCount(t *testing.T) {
	CharCount(strings.NewReader(`I love Go!!`))
}
