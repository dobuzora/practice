# ex3-10 辞書の作成
e2f = {
	'dog':'chien',
	'cat':'chat',
	'walrus':'morse',
	}
print(e2f)
# ex3-11 
print(e2f['walrus'])
# ex3-12
f2e = {}
for k,v in e2f.items():
	f2e[v] = k
print(f2e)
# ex3-13
print(f2e['chien'])
# ex3-14
english = set(f2e.values())
print(english)
