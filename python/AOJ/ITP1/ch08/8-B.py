# 数字の和
# 6/16
# pythonだと簡単
while True:
	num = list(map(int,*input().split()))
	#print(num)
	if num == [0]:
		break
	print(sum(num))

# 別解1
# iterはイテレータ (iterator) オブジェクトを返す
# 第２引数になるまで読み込む
# 理解不能！！
# おそらく 0 が現れるまで読み込み、読み込んだ値の合計を求めていると思われる
for str in iter(input, "0"):
	print(sum(int(c) for c in str))