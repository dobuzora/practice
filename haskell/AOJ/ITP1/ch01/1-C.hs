main = do
  -- I/Oアクション
  line <- getLine
  -- 読み込んだlineを要素ごとにリストに直し
  -- 型をInt型に変換してそれぞれリストにバインディング
  let [a,b] = map (\x -> read x::Int) $ words line
  -- 出力 showで文字列に直す
  putStrLn $ show (a*b) ++ " " ++ show ((a+b)*2)
