package treesort

import "strconv"

type tree struct {
	value       int
	left, right *tree
}

// ツリー内の値の列を見せる
func (t *tree) String() string {
	var list []int
	var str string
	appendValues(list, t)
	for _, v := range list {
		str += strconv.Itoa(v)
	}
	return str
}

// Sortはvalues内の値をその中でソートします
func Sort(values []int) {
	var root *tree
	for _, v := range values {
		root = add(root, v)
	}
	appendValues(values[:0], root)
}

// apendValuesはtの要素をvaluesの正しい順序に追加し、
// 結果のスライスを返します
func appendValues(values []int, t *tree) []int {
	if t != nil {
		values = appendValues(values, t.left)
		values = append(values, t.value)
		values = appendValues(values, t.right)
	}
	return values
}

func add(t *tree, value int) *tree {
	if t == nil {
		// return &tree(value : value}と同じ
		t = new(tree)
		t.value = value
		return t
	}
	if value < t.value {
		t.left = add(t.left, value)
	} else {
		t.right = add(t.right, value)
	}
	return t
}
