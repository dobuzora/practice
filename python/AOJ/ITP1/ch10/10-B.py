# 三角形
# 6/17
# プログラムじゃなくても面積を求められず、断念
# 数学の力が失われているようだ...

# 残りの辺を求めて、後は小学生でもわかる公式に当てはめるだけだったが
# 逆に難しく考えすぎていたようだ...
import math
a,b,C = map(float,input().split())
c = math.sqrt( (a*a)+(b*b) - 2*a*b*math.cos(C/180 * math.pi))
h = b * math.sin(C/180 * math.pi)
print(h * a /2)
print(a+b+c)
print(h)

# 参考1
import math
  
a, b, t = map(int, input().strip().split())
  
t = math.radians(t) # ラジアンに直す(piをかけなくてもよかったらしい)
h = b * math.sin(t)
l = a + b + math.sqrt(a*a + b*b - 2*a*b*math.cos(t))
s = a * h / 2
print(s)
print(l)
print(h)