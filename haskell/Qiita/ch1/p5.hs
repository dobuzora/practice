-- [問5] productを使ってfact( 階乗 )を実装してください

-- 再帰だと思い込んで結局独力でできなかった...
fact' n = product [1..n]

main = do
  print $ fact' 5