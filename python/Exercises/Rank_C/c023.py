num = input()
num = num.split()
counter = 0
count = input()
for i in range(0,int(count)):
	data = input()
	data = data.split()
	for j in range(0,6):
		if num[j] in data:
			counter += 1
	print(counter)
	counter = 0