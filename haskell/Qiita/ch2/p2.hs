-- [問2] x,y,w,h を 表現した Rect 型を定義して、Rect に Pointが含まれるか
-- どうかを判定する関数containsを実装してください

-- 理解すると簡単であったが、問題の意味が理解できず解けなかった

data Point = Point Int Int deriving Show
data Rect  = Rect Int Int Int Int deriving Show

contains (Rect x y w h) (Point px py ) = 
	x <= px && px < x + w && y <= py && py < y + h

main = do
  print $ contains (Rect 2 2 3 3) (Point 1 1)
  print $ contains (Rect 2 2 3 3) (Point 2 2)
  print $ contains (Rect 2 2 3 3) (Point 3 3)
  print $ contains (Rect 2 2 3 3) (Point 4 4)
  print $ contains (Rect 2 2 3 3) (Point 5 5)