# 練習問題1.4

重複した行を含むファイル名を表示

## 内容

まずいわせて欲しい、チュートリアルにしては難しすぎやしないだろうか...  

まず、簡単なテストファイルを用意した  
そこからdup2と同じ方法で、行をカウントした  

追加したのは新しい合成型を作り、キーをファイル名に値をそのファイルの行カウントのものを用意した  
あとは、同じ要領で重複した行を出力するのだが、その時にその重複行が含まれていたファイルを探し、出力した  
これで題意は満たせたのではないだろうか

~~~
$ go run main.go $(find test | grep -v test$)
map[perl:1 ruby:1 python:1 golang:1 php:1 c:1 c++:1 Swift:1]
map[raspberry:4 strawberry pi:1 strawberry:1 raspberry pi:1 orange:1]
map[peach:2 pear:4 orange:1 banana:1 mango:1]

------------------------

raspberry : 4
test/fruit2
pear : 4
test/fruit3
orange : 2
test/fruit2
test/fruit3
peach : 2
test/fruit3
~~~

結果から、orangeがfruit2とfruit3に含まれていたことがわかる