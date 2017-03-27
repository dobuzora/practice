# 練習問題4.2

デフォルトで標準入力のSHA256ハッシュを表示しろ  
フラグをつけて、SHA384ハッシュ、SHA512ハッシュを表示するコマンドラインフラグも作ろう

## 内容

コマンドフラグもつけて、ハッシュを生成するプログラムを作成した  
ただし、フラグを何もしていしないで実行するとパニックが起こる  
その場合の処理の方法がわからなかった  

~~~
$ go build main.go       
$ ./main golang          
d754ed9f64ac293b10268157f283ee23256fb32a4f8dedb25c8446ca5bcb0bb3
$ ./main -s sha384 golang
cbe229a7b014f56eb990414849d00ebd0f0add5be8ec3328d22767078dce25fefbc3bcaf3e1dba54a1f48e4a6b62531d
$ ./main -s=sha512 golang
df84c5d44709cfeb8a22c8cf006ac926c92c6823d37e112f2c68a22890e61615f97ad1d4eb1d3e043442063886b4ce2f15eaa73ea8ff769808fc76d47f607ec5
$ ./main                 
panic: runtime error: index out of range

goroutine 1 [running]:
~~~

テストや、バリデータもキチンと書きたい

## 参考

https://github.com/aconley/TheGoProgrammingLanguage/blob/master/src/exercises/gopl.io/ch4/sha/main.go