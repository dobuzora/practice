# ex3-8 リストも作成
surprise = list(('Groucho','Chico','Harpo'))
# ex3-9 
surprise[-1] = surprise[-1].lower() # 最後を小文字に
surprise[:] = surprise[::-1] # 逆順にして
surprise[0] = surprise[0].capitalize() # 元に戻す
print(surprise)
