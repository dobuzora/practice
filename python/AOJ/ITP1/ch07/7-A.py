# 成績
while(True):
	score = [int(i) for i in input().split()]
	if score[:] == [-1,-1,-1]:
		break
	if score[0] == -1 or score[1] == -1:
		print('F')
	else:
		score_sum = score[0] + score[1]
		if score_sum >= 80:
			print('A')
		elif 80 > score_sum >= 65:
			print('B')
		elif 65 > score_sum >= 50:
			print('C')
		elif 50 > score_sum >= 30:
			if score[2] >= 50:
				print('C')
			else :
				print('D')
		elif 30 > score_sum:
			print('F')

# 別解1

# だいたい処理の仕方は同じ、ただ、条件分岐は上から下へと進むため、
# 書かなくてもいい余計な条件を僕は書いていたようです...
while True:
    m, f, r = map(int, input().strip().split())
    if m == f == r == -1: break
    if m == -1 or f == -1 or m + f < 30:
        print('F')
    elif m + f >= 80:
        print('A')
    elif m + f >= 65:
        print('B')
    elif m + f >= 50:
        print('C')
    elif m + f >= 30:
        print('C' if r >= 50 else 'D')