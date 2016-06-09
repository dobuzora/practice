# M は立候補者の人数を、N は有権者の人数を、K は演説が行われる回数
num = list(map(int,input().split())) # 読み込み
election = {} # 辞書で管理
election = {i:0 for i in range(1,num[0]+1)}
election[0] = num[1]

def index_open(in_list):
	output = ''
	for i in in_list:
		output += str(i) + ' '
	print(output[:-1]) 
		

# 演説の読み込み
for i in range(num[2]):
	selec = int(input())
	count = 0
	for j in election.keys():
		if election[j] > 0:
			election[j] -= 1
			count += 1
	election[selec] += count

index_list = [] # オフセット
max_value = 0 # 最高値
# 辞書の各キーから最高値を求める
for i in range(1,num[0] + 1):
	if max_value < election[i]:
		max_value = election[i]
		index_list.clear()
		index_list.append(i)
	elif max_value == election[i]:
		index_list.append(i)
index_open(index_list)