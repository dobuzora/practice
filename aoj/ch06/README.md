再帰・分割統治法
===

## 全探索

全探索というタイトルから、再帰にどう結びつくかを考えたが再帰を使うことですべての組み合わせを探索するというもの。
正直、これはこれまでの自分にはかけないコードです。正解率50%超えに驚き。

Goで書くとこんな感じ。

```go
func solve(i int, m int) bool {
	if m == 0 {
		return true
	}
	if i >= n {
		return false
	}
	res := solve(i+1, m) || solve(i+1, m-A[i])
	return res
}
```

計算量はO(2^n)となる。

## コッホ曲線

難しいからお飛ばし。