-- [問4] 問2の解答をレコード構文で書き直してください

data Rect = Rect { rx :: Int, ry :: Int,rw :: Int,rh :: Int } deriving Show
data Point = Point { px :: Int, py :: Int } deriving Show

contains r p = 
  (rx r) <= (px p) && (px p) < (rx r) + (rw r) && 
  (ry r) <= (px p) && (py p) < (ry r) + (rh h)

main = do
  print $ contains Rect { rx = 2,ry = 2,rw = 3,rh = 3} Point {px = 1,py = 1}
  print $ contains Rect { rx = 2,ry = 2,rw = 3,rh = 3} Point {px = 2,py = 2}
  print $ contains Rect { rx = 2,ry = 2,rw = 3,rh = 3} Point {px = 3,py = 3}
  print $ contains Rect { rx = 2,ry = 2,rw = 3,rh = 3} Point {px = 4,py = 4}
  print $ contains Rect { rx = 2,ry = 2,rw = 3,rh = 3} Point {px = 5,py = 5}
