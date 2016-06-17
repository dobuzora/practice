# リング
# 6/17
# すぐにできた
string = input()
string = string*2
if string.count(input()):
	print("Yes")
else:
	print("No")

# 別解1
s, p = input() * 2, input()
# countではなくinを使って判定している
# また、後置のifを使って短くしている
print('Yes' if p in s else 'No')