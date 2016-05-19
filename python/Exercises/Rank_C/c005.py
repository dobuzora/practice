num = input()
for i in range(0,int(num)):
	ipaddr = input() # 読み込み
	ipaddr = ipaddr.split(".") # ドットで区切る
	
	# ドットで区切った後、区切り数が4でない時
	if len(ipaddr) == 4: 
		# 文字のチェック
		for j in range(0,4):
			# 数字かどうか、また3桁以内かどうか
			if ipaddr[j].isalnum() == True and len(ipaddr[j]) < 4:
				continue
			else:
				print("False")
				break
		else :
			print("True")
	else :
		print("False")
