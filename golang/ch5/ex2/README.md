# 練習問題5.2

 HTMLドキュメントツリー内でその要素名を持つ要素の数を対応させるマッピングのを行う関数を書きなさい

 ## 内容

 ex1のvisit関数を参考に、マップを用いて要素名とその数を対応させ、そのマップを返す関数countItemを実装した

 ~~~
$ go run fetch.go https://golang.org/ | go run main.go
     html : 1
   select : 1
   option : 8
       br : 3
   iframe : 1
     link : 3
   script : 10
        a : 22
     form : 1
 textarea : 2
      pre : 1
     head : 1
     meta : 3
     span : 3
    title : 1
     body : 1
      div : 33
    input : 1
~~~

