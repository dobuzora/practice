alpha = input()

point = 0
plus = 0
counter = 0
for i in range(4):
	if alpha[i] == '*':
		plus += 1
	else :
		if alpha.count(alpha[i]) >= point:
			point = alpha.count(alpha[i])
			counter += 1 # 4のときはツーペア

point = point + plus

if point == 1:
	print("NoPair")
elif point == 2 and counter == 4:
	print("TwoPair")
elif point == 2:
	print("OnePair")
elif point == 3:
	print("ThreeCard")
elif point == 4:
	print("FourCard")
else :
	print('Error')

