# 行列の積
# 6/16
# めちゃくちゃ頑張った！！
# 他の人の回答をみて絶望した...

# 読み込み処理
n,m,l = list(map(int,input().split()))
matrixA,matrixB = [],[]
for i in range(n):
	matrixA.append(list(map(int,input().split())))
for j in range(m):
	matrixB.append(list(map(int,input().split())))

# matrixBを計算しやすい形に変換
matrix = []
for i in range(l):
	mtr = []
	for j in range(m):
		mtr.append(matrixB[j][i])
	matrix.append(mtr)

# 行列Cを求める
matrixC = []
for i in range(l):
	mtr = []
	for j in range(n):
		num_sum = 0
		# print(matrixA[j],matrix[i])
		for a,b in zip(matrixA[j],matrix[i]):
			num_sum += a*b
		mtr.append(num_sum)
	matrixC.append(mtr)

# 形式にあった出力への変換
matrix = []
for i in range(n):
	out = ''
	for j in range(l):
		out += str(matrixC[j][i]) + ' '
	print(out[:-1])

# 別解1
from operator import mul # mul(a,b) == a * b
# function の引数が単一のiterable にタプルとして格納されている場合(“zip済み”)
# map()の代わりに使用します
from itertools import starmap

n, m, l = map(int, input().split())
a, b = ([tuple(map(int, input().split())) for _ in range(k)] for k in (n, m))
for line in ([sum(starmap(mul, zip(ai, bj))) for bj in zip(*b)] for ai in a):
    print(*line)

# 別解2
n, m, L = map(int, input().split())

# for _ のアンダーバーはリストから取り出すが、値は使わないよ！！っていう意味だと思う
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
c = [[sum(ak * bk for ak, bk in zip(ai,bj)) for bj in zip(*b)] for ai in a]

# アスタリスクでリストを綺麗に出力できる!?
for ci in c:
    print(*ci)

