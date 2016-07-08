cubic :: Int -> Int
cubic x = x * x * x

main = do
 x <- readLn
 print $ cubic x
