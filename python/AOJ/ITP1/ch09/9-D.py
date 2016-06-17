# 文字列変換
# 6/17
# できそうだと思ったが、一定の条件でスライスが期待通りの動きをしないため断念
# 誰かのコードを参考にした
# やろうとしていることは同じなんだけどな...

# 自分のコード
# 文字列はミュータブルであるため、リストで管理する
string = [str(i) for i in input()]
for _ in range(int(input())):
	n = input().split()
	order = n.pop(0)
	if order == 'replace':
		pass
	elif order == 'reverse':
		# どうやったら逆にできるのか...
		print(string[:int(n[0])],string[int(n[1]):int(n[0])-1:-1],string[int(n[1])+1:])
		#string  = string[:int(n[0])-1] + \
		#string[int(n[1]):int(n[0]):-1] + \
		#string[int(n[1])+1:]
	else :
		out = string[ int(n[0]) : int(n[1]) ]
		print(''.join(out))

# 作り直し
# リストで管理しなくてもよかった(大変!!)...
string = [str(i) for i in input()]
for _ in range(int(input())):
	n = input().split()
	order = n.pop(0)
	if order == 'replace':
		string = string[:int(n[0])] + \
		[i for i in n[2]] + string[int(n[1])+1:]
	elif order == 'reverse':
		string = string[:int(n[0])] + \
		string[int(n[0]):int(n[1])+1][::-1] + \
		string[int(n[1])+1:]
	else :
		out = string[ int(n[0]) : int(n[1])+1 ]
		print(''.join(out))

# 参考1
# 自作コードとアルゴリズムは同じ
# 逆にする方法がわからなかった
s = input()
  
for i in range(int(input())):
    cmd = input().split()
    # なるほど、これで数だけを抜き出したわけか
    a,b = [int(x) for x in cmd[1:3]]
  
    if cmd[0] == 'print':
        print(s[a:b+1])
    elif cmd[0] == 'reverse':
    	# s[a:b+1]で入れ替える文字列を生成してから、逆にしているのか！！
    	# 勉強になります
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif cmd[0] == 'replace':
        s = s[:a] + cmd[3] + s[b+1:]


        """