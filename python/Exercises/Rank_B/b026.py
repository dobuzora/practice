# 10点の問題
# 原因はある程度推測出来る。1つはお釣りを計算する段階で足りないことがわかっても
# それまででコインの個数を変えてしまっていることだろう

# 原因1
# ただし、50円硬貨、10円硬貨を組み合わせる、
# もしくはどちらか一方のみを使うことによって、
# おつりの内の100円分以上を返却することは許されません。

# 原因2
# また、おつりを返却することができない場合は購入不可能となり、
# それを知らせた上で投入された硬貨を全て返却します。

# 原因3
# 自動販売機の内部では、まずおつりとして返却された硬貨がなくなり、
# その後に投入された硬貨が貯まります。

# これらを考慮していないからだと思われる...

def print_name(p_list):
	p_str =''
	for n in p_list:
		p_str += str(n) + ' '
	print(p_str[:-1])

num = list(map(int,input().split())) # 読み込み
coin_list = [500,100,50,10]          # コインのリスト
coins = {k:v for k,v in zip(coin_list,num)} # 自販機の保持するコイン辞書
# 購入回数分for分を回す
for i in range(int(input())):
	input_value = list(map(int,input().split()))
	value = input_value.pop(0) # 商品の価格
	# いくらお金を投入したか
	sum_v = 0
	for m , i in zip(coin_list,input_value):
		coins[m] += i # 自販機の保有する金額を更新
		sum_v += m*i
	change = sum_v - value
	# お釣りを生成
	change_list = [0,0,0,0]
	coins_back = coins.copy()
	for j,n in zip(coin_list,range(4)):
		while coins[j] > 0:
			if change < j:
				break
			coins[j] -= 1
			change_list[n] += 1
			change -= j
	if change > 0:
		coins = coins_back
		print("impossible")
	else :
		count = 0
		for k,n in zip(change_list[2:],coin_list[2:]):
			count += n * k
			if k >= 10:
				print("impossible")
				break
			elif count >= 100:
				print("impossible")
		else :
			print_name(change_list)

