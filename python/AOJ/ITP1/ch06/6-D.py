# ベクトルと行列の積
# 6/19
# pythonの書き方がちょっとわかってきた
# 想定外に出会うことなく書き終えた

# 読み込み
col,row = map(int,input().split())
matrix = []
vector = []
# 行列読み込み
for _ in range(col):
	matrix.append([int(j) for j in input().split()])

# ベクトル読み込み
for _ in range(row):
	vector.append(int(input()))

# 演算処理
for i in range(col):
	ans = 0
	for x,y in zip(matrix[i],vector):
		ans += x * y
	print(ans)

# 別解1
# 驚くくらいほぼ同じ
(n, m) = [int(i) for i in input().split()]
A = []
b = []
for i in range(n):
    A.append([int(j) for j in input().split()])
  
for i in range(m):
    b.append(int(input()))
  
for i in range(n):
    s = 0
    for j in range(m):
        s += A[i][j] * b[j]
    print(s)
