# 構造化プログラミング
# 6/18
# 1行で書こうと調子に乗ったが、だめだった
# 参考を見たとき驚いた！！
# もっと広い視野で考えないとダメだと思った

# 自作コード(間違っている)
# ~3.* の処理ができなかった...
print(' ' + ' '.join(str(i) for i in range(1, int(input()) + 1) if i % 3 == 0 or i % 10 == 3 or i // 10 == 3))

# 修正コード
print(' ' + ' '.join(str(i) for i in range(1, int(input()) + 1) if i % 3 == 0 or '3' in str(i)))

# 参考1
# i の中に '3' がふくまれていると出力することに気が付かなかった、素晴らしい
# print(' ' + ' '.join(str(i) for i in range(1, int(input()) + 1) if not i % 3 or '3' in str(i)))

