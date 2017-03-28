# 練習問題4.9

入力テキストの中のそれぞれの単語の出現頻度を報告する

## 内容

ヒントがあったため、非常に実装しやすかった  
新たな発見は、`input.Split(bufio.ScanWords)`でワードごとにスキャンできたことに驚いた  

~~~
$ go run main.go test 
Get : 1
knees! : 1
Beg : 1
You : 1
are : 1
me : 1
life! : 1
to : 1
your : 2
going : 1
on : 1
for : 1
get : 1
that : 1
stone! : 1
~~~

