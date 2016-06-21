# ミンコフスキー距離
# 6/17
# pow を 使わずに ** (1/3) でもできた
# 全く考えていなかった
import math

Manhattan = 0
Euclid = 0
Three = 0
Chebychev = []
num = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

# マンハッタン距離
for i in range(num):
	Manhattan += math.fabs(x[i] - y[i]) 
	Euclid += math.fabs((x[i] - y[i])**2)
	Three += math.fabs((x[i] - y[i])**3)
	Chebychev.append(math.fabs((x[i] - y[i])))

print(Manhattan)
print(math.sqrt(Euclid))
print(math.pow(Three,1/3))
print(max(Chebychev))

# 別解
# 関数で処理をするのは賢いやり方だと思った
# 確かに、重複してるところが多々ある
def minkowsuki(x, y, n):
    return sum(abs(x[i] - y[i]) ** n for i in range(len(x))) ** (1 / n)
 
n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
 
print(minkowsuki(x, y, 1))
print(minkowsuki(x, y, 2))
print(minkowsuki(x, y, 3))
print(max(abs(x[i] - y[i]) for i in range(n)))