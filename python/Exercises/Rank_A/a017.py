'''
・1 行目には 3 つの整数 H, W, N がこの順に半角スペース区切りで与えられます。
　H はフィールドの縦幅を、W はフィールドの横幅を、 N は落ちてくる長方形の個数を表します。
・続く N 行のうち i 行目 (1 ≦ i ≦ N) には i 番目に落ちてくる長方形のサイズと落ちてくる位置の情報が入力されます。
　ここではこの長方形の縦幅 h_i、横幅 w_i、長方形の左端とフィールドの左端の距離 x_i がこの順に半角スペース区切りで与えられます (問題文中の図を参照)。
・入力は合計で N + 1 行であり、入力最終行の最後に改行が 1 つ入ります。
'''

'''
・期待する出力は H 行からなります。
・出力の i 行目 (1 ≦ i ≦ H) にフィールドの上端から距離 i の各地点の状態を表す長さ W の文字列 f_i を出力してください。
　　f_i の j 番目 (1 ≦ j ≦ W) の文字は、フィールドの上端、左端からの距離が i, j となる地点の状態を表し、ここにブロックがあるときは "#"、ないときは "." となります。
・出力の H 行目の最後に改行を 1 つ入れ、余計な文字、空行を含んではいけません。
'''
from pprint import pprint

def create_Rectangle(h,w,x):
	global field
	x_flag = False # xの位置が決定したかどうかのフラグ
	flag = False   # 描画フラグ
	x_point = []
	# 長方形を描く処理
	for i in range(f_h-1,-1,-1):
		for j in range(f_w):

			# main処理 #######################

			# 配置のポイント探し

			# xポイントフラグ
			if x_flag == False:
				# xのポイントに来た時、'#'がなければ！！
				if j == x and field[i][j] != '#':
					x_flag = True
					x_point = [i,j]

			# ポイントフラグが立っていないと何もしない
			if not x_flag:
				continue
			else :
				# 描画フラグ
				if j == x_point[1]:
					flag = True
				# 高さの残りがない時はフラグをOFFにする
				if h == 0:
					flag = False

				# フラグが立っている時(ブロックを描画する時)
				if flag == True:
					if j < x+w :
						field[i][j] = '#'
					else :
						flag = False
						h -= 1



			#################################		
	return 0

# 読み込み
f_h,f_w,n = list(map(int,input().split()))
field = []
# フイールドの生成
for i in range(f_h):
	f_list = []
	for j in range(f_w):
		f_list.append('.')
	field.append(f_list)

# 各データの読み込み
for j in range(n):
	h,w,x = list(map(int,input().split()))
	create_Rectangle(h,w,x)
	
pprint(field)
