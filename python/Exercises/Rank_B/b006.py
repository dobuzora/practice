import math
G = 9.8

# 読み込み
num = input()
o_y,s,theta = map(float,num.split())
num = input()
x,y,space = map(float,num.split())

# 命中位置計算
y_after = o_y + (x * math.tan(theta/180*math.pi)) - ((G*x**2)/(2*s**2*math.cos(theta/180*math.pi)**2))
y_after = (round(y_after*10))/10 # 小数点の処理
#print(y_after)

# 判定
if y_after > 0: # 命中地点が正のとき
	under = (y - space/2) # 的の中心より下の部分
	# 負の値になった場合、地面までの距離を計算
	if under < 0:
		under = space/2 + under
	if under < y_after < (y + space/2):
		ans = 'Hit' + ' ' +  str(round((math.fabs(y - y_after)*10))/10)
	else:
		ans = 'Miss'
else:
	ans = 'Miss'
print(ans)