# 挿入ソート
# 6/24
# 頭を使わず、言われたままに作った

num = int(input())
sort_list = list(map(int,input().split()))
print(*sort_list)
v = 0
for i in range(1,num):
	v = sort_list[i]
	j = i - 1
	while j >= 0 and sort_list[j] > v:
		sort_list[j+1] = sort_list[j]
		j -= 1
		sort_list[j+1] = v
	print(*sort_list)
