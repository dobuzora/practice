xc,yc,r1,r2 = map(int,input().split())
r1 *= r1
r2 *= r2
for _ in range(int(input())):
	x,y = map(int,input().split())
	dein = (x - xc)**2 + (y - yc)**2
	if r1 <= dein <= r2:
		print("yes")
	else :
		print("no")