-- elem関数の再現
--
-- ギブアップ！


-- \= は not equal
myElem val myList = (length filteredList) /=0  where filteredList = filter (==val) myList

