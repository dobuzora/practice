tagA,tagB = map(str,input().split())
string = input()

end = 0
while True  :
	index = string.find(tagA,end)
	if index == -1:
		break
	end = string.find(tagB,index)
	out = string[index+len(tagA):end]
	if out == '':
		print("<blank>")
	else:
		print(out)