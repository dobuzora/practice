# 90点
# どこかに修正ポイント

# 入力値より辞書を作る関数
def input_dict():
	alpha_map = input()
	alpha_map = map(int,alpha_map.split())
	alpha_dict ={}
	for i,name in enumerate(alpha_map,1):
		alpha_dict[i] = name;
	return alpha_dict

# 準備
num = input()
num = num.split()
A_dict = input_dict()
B_dict = input_dict()

offside = [] # オフサイド背番号を格納するリスト
# Aがパスを出す時
if num[0] == 'A':
	enemy = 0
	# 2番目のやつの座標を取得
	for y in sorted(B_dict.values(),reverse=True):
		enemy = enemy + 1
		if enemy == 2:
			enemy = y
			break
	# Aチームの座標求める
	for x in A_dict.keys():
		# 敵陣にいるやつ
		if A_dict[x] >= 55 :
			# 2番目の敵より向こうにいる、かつパスを出すやつより敵陣にいる
			if enemy < A_dict[x]:
				offside.append(x)
# Bがパスを出す時
elif num[0] == 'B':
	enemy = 0
	for y in sorted(A_dict.values()):
		enemy = enemy + 1
		if enemy == 2:
			enemy = y
			break
	for x in B_dict.keys():
		if B_dict[x] <= 55 :
			if enemy > B_dict[x]:
				offside.append(x)

if not offside:
	print('None')
else :
	for z in offside:
		print(z)
