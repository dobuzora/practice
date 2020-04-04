inFirstHalf val myList = val `elem` firstHalf
  where midpoint = (length myList) `div` 2
        firstHalf = take midpoint myList
