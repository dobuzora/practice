# ex3-4 リストの作成
things = list(('mozzarella','chinderella','salmonella'))
print(things)
# ex3-5 人の名前を大文字にせよ
print(things[things.index('chinderella')].capitalize())
# print(things) # 変わらない...リストの要素を変えるには代入する
# ex3-6 リストの中のチーズを大文字にして表示せよ
print(things[things.index('mozzarella')].title())
# ex3-7 リストから病気を削除する
things.remove('salmonella')
print(things) # 削除された