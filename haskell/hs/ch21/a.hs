-- Atcoder


checkString :: String -> String
checkString str = str ++ "!"

main :: IO ()
main = do
  str <- getLine
  let ans = checkString str
  putStrLn ans
