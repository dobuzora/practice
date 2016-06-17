# 文字のカウント
# 6/16
# 回答を見ました！！
# 辞書を使ってやろうと考えていたけど、できなかった
# よく考えると今までinput()は回数分for文をまわしていたので、
# 一行しか読むことができず、できないことは当たり前だった...
import sys

s = str()
alpha = "abcdefghijklmnopqrstuvwxyz"

# for line in input() としていたが、それだと1行しか読めない
for line in sys.stdin:
    s += line.lower()
 
for c in alpha:
    print(c+" : "+str(s.count(c)))