num = input()
kabu_list = []
# 読み込みループ
for i in range(int(num)):
	kabu = input()
	kabu_list.append(kabu.split())

kabu_max = 0
for i in kabu_list:
	if kabu_max < int(i[2]):
		kabu_max = int(i[2])

kabu_min = 1000000
for i in kabu_list:
	if kabu_min > int(i[3]):
		kabu_min = int(i[3])
print(kabu_list[0][0],kabu_list[int(num) - 1][1],kabu_max,kabu_min)