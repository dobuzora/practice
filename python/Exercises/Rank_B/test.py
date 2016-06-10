length = int(input())
string_list = [s for s in input()]

left = string_list[0]
right = string_list[-1]

if left == right:
	if left == "w":
		print(0)
	else :
		print(length)
else :
	if string_list.count("w") > string_list.count("b"):
		print(string_list.count("b")-1)
	elif string_list.count("w") < string_list.count("b"):
		print(string_list.count("b")+1)
	elif string_list.count("w") == string_list.count("b"):
		print(string_list.count("b"))