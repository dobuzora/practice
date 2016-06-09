# coding: utf-8
num = int(input())
for n in range(0,num):
	input_lines = input()
	odd = 0 # 初期化
	even = 0 #初期化
	# 奇数桁
	for m in input_lines[1:14:2]:
		odd += int(m)
	# 偶数桁
	# 2倍した総和
	for k in input_lines[0:15:2]:
		p = int(k)*2 # 2倍する
		# 2桁かどうかチェック
		if p > 9: 
			sub = 1 + p%10
			even += sub
		else:
			even += p
	if ((odd + even) % 10) == 0:
		print('0')
	else:
		print(10 - ((odd + even) % 10))