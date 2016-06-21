# 標準偏差
# 6/17
# 正直よくわからなかったが、式の通り実装すればできた
from math import sqrt

while True:
	input_data =[] # 格納リスト
	alpha = 0 # 回答
	num = int(input())
	if num == 0:
		break
	input_data = [float(i) for i in input().split()]
	m = sum(input_data) / float(num)
	for i in range(num):
		# アクセスしなくても、input_dataの要素を取り出していけばよかった
		alpha += (input_data[i] - m)**2
	print(sqrt(alpha/num))

# 別解1
# 見習う場所あり
import math
 
while True:
    n = int(input())
    if n == 0:
        break
    data = [int(n) for n in input().split()]
    ave = sum(data) / len(data)
    var = 0
    for s in data:
        var += (s - ave) ** 2
    print(math.sqrt(var / len(data)))