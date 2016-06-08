# 原因不明の0点
# テストもクリアするのになぜ？

num = input() # 0,2がそれぞれ個数と円の半径
radius = int(num[2])
for i in range(int(num[0])):
	input_value = input()
	input_value = list(map(int,input_value.split()))
	for j in input_value:
		if j < radius:
			break
	else:
		print( i + 1)