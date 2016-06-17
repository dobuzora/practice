# シャフル
# 6/17
# ギブアップ！！
# 惜しいけど、できない！！
# 原因はいくつ移動するか計算するときに、一周すると狂ってしまうから


# 参考に作り直したコード
while True:
	string = input()
	if string == '-':
		break
	# 読み込む数
	for i in range(int(input())):
		num = int(input())
		string = string[num:] + string[:num]
	print(string)


# 参考1
while True:
    cards = input()
    if cards == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        # スライスで随時更新してるみたい
        cards = cards[h:] + cards[:h]
    print(cards)
