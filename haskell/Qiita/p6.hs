-- [問6]点(p,q)から直線 ax + by = c に下した垂線の交点を求める関数perpPoint
-- を作成してください
-- aとｂが両方ゼロになると解なしですが、チェックはせずに無視してください

-- コード・計算ともに難しかった...
-- whereを使ってまとめることができた
perpPoint (p,q) (a,b,c) = (x,y)
  where
  	x = (a*c + b*d) / (a*a + b*b)
  	y = (b*c - a*d) / (a*a + b*b)
  	d = b*p - a*q

main = do
  print $ perpPoint (0,2) (1,-1,0)