 # 満点コード
 # ミスは8行めの// を /　としていたことと、細かい条件間違い

num = list(map(int,input().split()))

def time_creater(answer):
	output = '0' + str(answer[0]) + ':'
	if answer[1] // 10 > 0:
		output += str(answer[1])
	else :
		output += '0' + str(answer[1])
	print(output)

def calc_time(cal,t_sum):
	cal[1] -= t_sum
	if cal[1] < 0:
		cal[0] += (cal[1] // 60)
		cal[1] = -(60*(cal[1] // 60)) + cal[1]
	return cal
 

ans = [0,0]
train = []
for i in range(int(input())):
	in_put = list(map(int,input().split()))
	in_put[1] += (num[1] + num[2]) # 分を足す
	# 60を超える場合
	if in_put[1] >= 60:
		in_put[0] += (in_put[1] // 60) # 時間を増やす
		in_put[1] = in_put[1] % (60*(in_put[1] // 60))
	if ans[0] <= in_put[0] < 9:
		if ans[1] <= in_put[1] < 60 :
			ans = in_put
# 出発時間を求める
ans = calc_time(ans,(num[1]+num[2]))
ans = calc_time(ans,(num[0]))
time_creater(ans)

