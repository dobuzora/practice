# 公舎の入居者数
# 6/18


# 指定のリストを作る関数
def create_List():
	re_list = [[],[],[],[]]
	for i in range(4):
		for j in range(3):
			re_list[i].append([0 for k in range(10)])
	return re_list

# 配列で全て読み込んでから表示しよう(方針)
num = create_List()
for _ in range(int(input())):
	data = list(map(int,input().split()))
	num[data[0]-1][data[1]-1][data[2]-1] += data[3]

# 出力処理
for i in range(4):
	for j in range(3):
		print(' ' + ' '.join(map(str,num[i][j])))
	if i == 3:
		break
	print('#'*20)


# 別解1
data = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
n = int(input())
for _ in range(n):
    (b, f, r, v) = [int(i) for i in input().split()]
    data[b - 1][f - 1][r - 1] += v
   
for b in range(4):
    for f in range(3):
        for r in range(10):
            print('', data[b][f][r], end='')
        print()
    if b != 3:
        print('#' * 20)