# 練習問題7.2

 `func CountingWriter(w io.Writer) (io.Writer, *int64)` のシグニチャを持つ関数を書きなさい

 ## 内容

現状の力では、この問題を解くことができなかった  
公式の解答はないので（欲しいよ〜）、すでに解答している人のコードを参考に学習した  

渡す`io.Writer`は7.1で用いたByteCounterで、これは自分に渡されたバイトスライスのバイト数を書き込む  
このByteCounterをCountingWriter関数に渡すと、`io.Writer`を包む新たな型countingWriter型の構造体が作られそれらを返す  

また、`io.Wirter`を返すにはcountingWriter型を`io.Writer`にしなければならない  
そこで、countingWriterに書き込みバイト数とエラーを返すWriterメソッドを定義した  

*動作確認*
~~~
$ go run main.go
c = 37
==== Next Step =====
c = 74
b = 37
~~~

最初はcに書き込まれたバイト数は37である  
次にCounterWriter関数呼び出したのち、同じ処理を行うとcは同じバイト数が書き込まれ74となる  
`io.Writer`を包んでいるcountingWriterは、新たに書き込まれたバイト数を記録するため34となっている  
そのため、正しく動作していると思う...

## 振り返り

*失敗1*  
渡された`io.Writer`をwrapする新たなWriterを返すという部分は、これは新しい型が必要になることを意味している  
しかし、そもそも、新しい型が必要という考えに至らなかったのが、根本的な失敗

*失敗2*  
渡された`io.Writer`を包むという意味が理解できていなかった  
仮に包めたとしても、包んだらそれは`io.Writer`にはならないのではという考えを持っていた  
これは失敗1にも起因する（そもそも新しい型を作ろうとする考えがなかった）が、構造体を宣言して`io.Writer`というフィールドを持った`io.Writer`を作ろうという意味であった  
また、包んだ構造体をどうやって`io.Writer`型にするのかも考えれなかっただろう(Writeメソッドを定義)

*失敗3*  
これは失敗ではないが、たとえ上の２つが分かったとしても、はたしてコード化することができたかという問題もある  

7.2は歯が立たなかったというのが事実であるが、悩み抜いて他人のコードを見たことで理解が大きく深まった  
非常によい勉強になった

### 参考
https://github.com/aconley/TheGoProgrammingLanguage/blob/master/src/exercises/gopl.io/ch7/counters/countingwriter.go