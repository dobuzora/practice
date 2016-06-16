# 6/16 アルゴリズムが思いつかず断念
# 他の方のものを解読した
# itertoolsでconbinationを求められることがわかった

while True:
	n,x = list(map(int,input().split()))
	if n == 0 and x == 0:
		break

	count = 0
	for a in range(1,x//3):
		for b in range(a+1,x//2):
			c = x - (a + b)
			if b < c <= n:
				count += 1
	print(count)

# 参考1
while True:
    n, x = map(int, input().split())
    # 終了条件
    # 私は if n == 0 and x == 0 と書くかこの書き方でもOK
    if n == x == 0: 
        break

    result = 0
    # 求める値xの3分の1までの数のループ
    for a in range(1, x // 3):
    	# 求める値の半分までのループ
        for b in range(a + 1,  x // 2):
            c = x - a - b # a,bからcを求める
            if b < c <= n: # チェック
                result += 1
                print(a,b,c)
    print(result)

# 参考2
from itertools import combinations
# itertoolsモジュールはイテレータを構築する部品を実装している
 
while True:
    n, x = map(int, input().strip().split(exi))
    if n == x == 0: break
    # ()であるためジェネレータ内包表記
    # conbinationsで組み合わせを求めてその合計を求め、xならば1のジェネレータを生成している
    # それを最後に合計すれば数が求めるという寸法...すごいな...
    print(sum(1 for p in combinations(range(1, n + 1), 3) if sum(p) == x))