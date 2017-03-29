# 練習問題5.1

ループの代わりに、visitへの再帰呼び出しを使って`n.FirstChild`リンクリストを走査するよう書き換えなさい

## 内容

これもかなり苦戦した問題  
なんとなくの構造は頭で構築できていたが、エラーに阻まれた  
またその原因の特定にも時間がかかったため、結果悪戦苦闘する羽目となった

~~~
$ go run fetch.go https://golang.org/ | go run main.go
/
/
#
/doc/
/pkg/
/project/
/help/
/blog/
http://play.golang.org/
#
#
//tour.golang.org/
https://golang.org/dl/
//blog.golang.org/
https://developers.google.com/site-policies#restrictions
/LICENSE
/doc/tos.html
http://www.google.com/intl/en/policies/privacy/
~~~

苦戦した割に、エラーの回避は至極単純で、関数の頭で渡された値が nil だったなら何もせずに links を返す処理を加えるだけであった  
エラーの原因は nil が渡されていたことだった

単純なことに嵌った反省としては、頭だけで考えず紙などを用いて考えることが近道だったということ

**追記**
NewSiblingを一回しか呼び出していないということは、弟しか調べていないのでは...
コード間違ってそうだけど、先を急がないといけないので、許して
