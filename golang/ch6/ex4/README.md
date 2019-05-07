# 練習問題6.4

rangeループに適した、セットの要素を含むスライスをかえすElemsメソッドを追加しなさい

## 内容

はじめに目標を先に決めます  
現状色々メソッドが増えて、便利になっているが結果を出力しかできないので、結果をスライスで返すメソッドを作る  

`[]int`型のスライスを返すメソッドを作った
仕組みはString()メソッドをほぼ真似て、文字列をint型に直しスライスに追加するというものである