-- [問1]任意のn番目のフィボナッチ数を計算sる関数fibを
-- パターンマッチで実装しなさい

fib 0 = 0
fib 1 = 1
-- nが1以上のとき, n-1とn-2の値を足す
fib n | n > 1 = fib ( n - 2 ) + fib ( n - 1 ) 

main = do
  print $ fib 6
