# 距離
# 6/17
# 数学ができれば楽にとける
import math

x1,y1,x2,y2 = map(float,input().split())
print(math.fabs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)))

# 別解1
# ユークリッドノルム(sqrt(x*x + y*y))を返します
# これは原点から点 (x, y) のベクトルの長さ
from math import hypot
  
x1, y1, x2, y2 = map(float, input().strip().split())
# 知っていればこっちの方が楽
print(hypot(x2 - x1, y2 - y1))