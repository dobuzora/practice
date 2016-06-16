# 表計算
# とくに問題なくクリア
# リストの出力には改善の余地がありました

r,c = list(map(int,input().split()))
matrix = []
for i in range(r):
	matrix.append(list(map(int,input().split())))
	matrix[i].append(sum(matrix[i]))
add_list = []
for j in range(c+1):
	num = 0
	for k in range(r):
		num += matrix[k][j]
	add_list.append(num)
matrix.append(add_list)

for i in range(r+1):
	out = ''
	for m in matrix[i]:
		out += str(m) + ' '
	print(out[:-1])


# 別解1
(r, c) = [int(i) for i in input().split()]
src = []
for _ in range(r):
    row = [int(i) for i in input().split()]
    row.append(sum(row))
    src.append(row)
last_row = [0 for _ in range(c + 1)]
for rc in range(r):
    for cc in range(c+1):
        last_row[cc] += src[rc][cc]
src.append(last_row)
  
for rc in range(r+1):
	# 便利!!短い!!やってることはあんまり変わらなんだけどね
    print(' '.join([str(a) for a in src[rc]]))


# 別解2
raws, columns = map(int, inpn ut().strip().split())
a = []
for i in range(raws):
    a.append(list(map(int, input().strip().split())))
for i in range(raws):
    a[i].append(sum(a[i]))
# zipのアスタリスクは何をしてるの？
a.append([sum(i) for i in zip(*a)])
for r in a:
    print(' '.join(str(x) for x in r))