nsp = input().split()
carrot = [] # 1.番号 2.質量 3.許容値
mount = 0 # 目的の番号を取得
limit_max = int(nsp[1]) + int(nsp[2]) # 許容最大値
limit_min = int(nsp[1]) - int(nsp[2]) # 許容最小値

for i in range(0,int(nsp[0])):
	element = input()
	# 許容値チェック
	if limit_min <= int(element.split()[1]) <= limit_max:
		carrot.append(str(i+1) + " " + element)

# 許容値を超えるものが１つしかない場合 -> その番号を保存
if len(carrot) == 1 :
	mount = int(carrot[0].split()[0])
# 全て許容値を超えない場合 -> 何もしない
elif len(carrot) == 0:
	pass
# 許容値を超えるものが複数存在した場合
else :
	mass = int(carrot[0].split()[1])
	mount = int(carrot[0].split()[0])
	for j in range(0,len(carrot)):
		# 質量の大きい人参を探索
		if mass < int(carrot[j].split()[1]):
			mass = int(carrot[j].split()[1])
			mount = int(carrot[j].split()[0])

if mount == 0:
	print("not found")
else:
	print(mount)