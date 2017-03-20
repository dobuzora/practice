# 練習問題1.10

大量のデータを生成するwebサイトを見つけ、キャッシュされているか調査  
また、出力をフィアルへ保存する

## 内容

キャッシュについては、計測結果からされていないと思われる  
また、ファイルの出力についてはこれもまた文脈の意図が汲み取れず、結果をファイル出力するか取得コンテンツをファイル出力するのか不明であった  
今回は、結果をリザルトファイルに出力した

いちいち新しいファイルが生成されて過去のデータが消えるので、追加するような形に修正したい

~~~
$ go build main.go
$ ./main $(cat urls)
$ cat result 
0.19s   37266 http://www.apple.com/jp/
0.26s   42101 http://syosetu.com/
0.68s   69117 http://gigazine.net/
1.09s  221438 https://www.amazon.co.jp/
1.09s elapsed
$ ./main $(cat urls)
$ cat result 
0.09s   37266 http://www.apple.com/jp/
0.10s   42143 http://syosetu.com/
0.20s   69117 http://gigazine.net/
1.02s  241925 https://www.amazon.co.jp/
1.02s elapsed
~~~