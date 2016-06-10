# 10点からなんとか100点まで上げた
# 目先で解こうと躍起になっていたが、アルゴリズムが大切だということに気づいた

import sys

length = int(input())
string_list = [s for s in input()]

def convert(st_list,le,ri):
	for n,k in enumerate(st_list[le:ri]):
		if k == 'w':
			st_list[n+le] = 'b'
		elif k == 'b':
			st_list[n+le] = 'w'
	return st_list

left = string_list[0]
right = string_list[-1]

if left == right:
	if left == 'w':
		print(0)
		sys.exit()
	elif left == 'b':
		print(length)
		sys.exit()

while True:
	for i,j in zip(range(length),string_list):
		if left != j:
			l_i = i
			break
	for i_,j_ in zip(range(length,0,-1),string_list[::-1]):
		if right != j_:
			r_i = i_
			break
	if l_i == r_i:
		break
	string_list = convert(string_list,l_i,r_i)

print(string_list)
print(string_list.count('b'))