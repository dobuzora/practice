-- [問8] バブルソートを実装してください
-- ヒント 交換する関数をソートする関数を分離して実装する

-- 頑張った痕跡...

-- 交換する関数
-- exchange' x (y:ys) = y:x:ys
-- ソートする関数
-- sort' [] = []
-- sort' (x:y:ys) 
--   | x > y = exchange' x (y:ys)
--   | otherwise = x : sort' (y:ys)
-- main = do
--   print $ sort' [4,1,5,3,2]
--   --print $ b_sort [3,1,5,7]


-- 引数リストの要素が1つならそのまま
bswap [x] = [x]
-- 引数リストの要素が2つ以上なら
bswap (x:xs)
  -- x のほうが大きければ入れ替える
  | x > y = y:x:ys
  -- そうでなければそのまま
  | otherwise = x:y:ys
  -- 
  where
  	(y:ys) = bswap xs

-- 引数リストが空なら空リストを返す
bsort [] = []
bsort xs = y : bsort ys
  -- xs は　引数リスト
  -- ここでbswapしたものの最初を y その他を ys で表している
  where
  	(y:ys) = bswap xs

main = do
	print $ bswap [4,3,1,5,2]
	print $ bsort [4,3,1,5,2]
	print $ bsort [5,4,3,2,1]
	print $ bsort [4,6,9,8,3,5,1,7,2]