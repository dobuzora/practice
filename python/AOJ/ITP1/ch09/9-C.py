#カードゲーム
# 6/17
# 辞書順でということは単語を認識しないといけないよいうだ:ミス1
# 単語の長さからの辞書の順番を考慮していなかった
# 独力で完成したものの、30分以上時間がかかった...

point_a,point_b = 0,0
# ループ
for i in range(int(input())):
	k =[]
	a,b = input().split()
	# 内包表記で、互いに違う文字が現れる場所を探り記録する
	k = [[i,j] for i,j in zip(a,b) if i != j]
	# kに何もないときは、全く同じワードもしくは部分的に同じワード
	if k == []:
		# 長さが長い方が辞書的には大きいことになる
		if len(a) < len(b):
			point_b+=3
		elif len(a) > len(b):
			point_a += 3
		else:
			point_a+=1
			point_b+=1
	# 最初のアルファベットの違いを検出
	elif ord(k[0][0]) < ord(k[0][1]):
		point_b += 3
	else :
		point_a += 3
print(point_a,point_b)

# 別解1
# 私のコードより、条件分岐が少ない
# 文字列を大小比較できるのか！！って驚いた
# 文字列の場合は比較する2つの文字列をアルファベット順に並べて比較する
# 「a」は「b」よりも小さく「A」は「a」よりも小さい
n = int(input())
 
T_s = 0
H_s = 0
 
for i in range(n):
    animals = input().split()
    T_a = animals[0]
    H_a = animals[1]
    if T_a < H_a:
        H_s += 3
    elif T_a > H_a:
        T_s += 3
    else:
        T_s += 1
        H_s += 1
 
print(T_s, H_s)