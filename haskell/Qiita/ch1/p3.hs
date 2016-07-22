-- [問3]問1で実装した関数をcase - of で書きなおしてください

-- case - of では = ではなく -> を使う
-- ちょっと独特の使い方
fib n = case n of
  0 -> 0
  1 -> 1
  _ | n > 0 -> fib (n-1) + fib (n-2)

main = do
  print $ fib 6