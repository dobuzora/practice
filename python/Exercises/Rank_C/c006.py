# 一部不正解を検出
# 原因解析中

init = input() # 読み込み
init = init.split() # 0.パラメータ 1.ユーザ人数 2.トップK
score = input() #読み込み
score = score.split()
rank_list = [] # ランキングリスト

# ユーザ数だけループを回す
for i in range(0,int(init[1])):
	data = input() # データ読み込み
	data = data.split()
	point = 0 # ポイントの初期化

	# パラメータの数だけループを回す
	for j in range(0,int(init[0])):
		point += int(data[j]) * float(score[j])

	rank_list.append(round(point)) # 四捨五入してリストに追加

rank_list = sorted(rank_list,reverse = True) # リストをソート

# トップ数だけループを回しランキングを表示
for k in range(0,int(init[2])):
	print(rank_list[k])