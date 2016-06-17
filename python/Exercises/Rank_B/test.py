length = int(input())
string_list = [s for s in input()]

left = string_list[0]
right = string_list[-1]
print(string_list)

if left == right:
	if left == "w":
		print(0)
	else :
		print(length)
else :
	w = string_list.count("w")
	b = string_list.count("b")
	if w > b:
		print(b - (b - w))
	elif w < b:
		print(b + (b - w))
	elif w == b:
		print(b)