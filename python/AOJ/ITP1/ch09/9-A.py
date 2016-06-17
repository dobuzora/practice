# 単語の検索
# 6/17
# 簡単に終わると思いきや、ちょっと手こずった
# count()だと、予期しない場所にもマッチしてしまうため、
# split()でワードごとにcount()を行った

import sys

match = input().lower()

s = str()
for line in sys.stdin:
	s += line.lower()
print(s.split().count(match))

# 別解1
# 同じようなコード
# しかし、countを使わずに行っている
import sys
 
keyword = input().lower()
count = 0
for line in sys.stdin:
    count += sum([1 for word in line.lower().split() if word == keyword])
     
print(count)