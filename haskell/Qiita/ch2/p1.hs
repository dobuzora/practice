-- [問1] 光の三原色と、2つの色を混合する関数mixを定義してください.
-- 混ぜることによってできる色も定義の対象とします.
-- ただし同じ成分同士は強めあわないもとします.

-- データ型を定義
data Color = Blue | Red | Magenta | Green | Cyan | Yellow | White
  deriving (Show,Eq)

-- 2つの色を混合する関数mix
mix Blue Red = Magenta
mix Blue Magenta = Magenta
mix Blue Green = Cyan
mix Blue Yellow = White
mix Red  Magenta = Magenta
mix Red Green = Yellow
mix Red Cyan = White
mix Red Yellow = Yellow
mix Magenta Green = White
mix Magenta Cyan = White
mix Magenta Yellow = White
mix Green Cyan = Cyan
mix Green Yellow = Yellow
mix Cyan Yellow = White
mix White  _     = White
-- 逆の組み合わせも一括処理
mix c1 c2 | c1 == c2 = c1
          | otherwise = mix c2 c1

main = do 
	print $ mix Blue Blue
	print $ mix Red Blue
	print $ mix Blue Green