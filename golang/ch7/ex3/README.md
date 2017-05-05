# 練習問題7.3

*tree型に対して、ツリー内の値の列を見せるStringメソッドを書きなさい

## 内容

はじめからあったものは、Sort関数を呼び出した時に結果を出力するというものである   
Sort関数呼び出し前はtreeに値は入っていないが、一度Sort関数を呼び出した後だとtreeに値がセットされている  


目指すべき動作はSort関数を類似しているため、 Sort関数を参考にした  

題意を確実に満たしたという自信はないが、こんなところではないだろうか...  

~~~
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
~~~