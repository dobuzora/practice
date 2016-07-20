-- [問4]sum,product,take,drop,reverseと同じ機能の
-- 関数を実装してください

-- リストが空なら0を返す
length' [] = 0
-- リストの2番目の要素があれば再帰処理
length' (_:xs) = 1 + length' xs

-- リストが空なら0を返す
sum' [] = 0
-- リストの１つめを足し、残りリストを再帰処理
sum' (x:xs) = x + sum' xs

-- リストが空なら0を返す
product' [] = 1
-- リストの1つ目を掛け、残り野リストを再帰処理
product' (x:xs) = x * product' xs

-- リストが空なら空リストを返す
take' _ [] = []
-- n が1以下ならば空リストを返す
take' n _ | n < 1 = []
-- 空リストに１つずつ取り出した値を挿入する 
take' n (x:xs) = x : take' ( n - 1 ) xs

-- リストが空なら空リストを返す
drop' _ [] = []
-- ｎが1以下なら残りのリストを返す
drop' n xs | n < 1 = xs
-- nが0になるまで再帰
drop' n (_:xs) = drop' ( n - 1 ) xs

-- リストが空なら空リストを返す
reverse' [] = []
-- 後ろから追加することで逆順に成る
reverse' (x:xs) = reverse' xs ++ [x] 


main = do
  print $ length' [1,2,3]
  print $ sum' [1,2,3]
  print $ product' [1,2,3] 
  print $ take' 2 [1,2,3]
  print $ drop' 2 [1,2,3]
  print $ reverse' [1..5]
