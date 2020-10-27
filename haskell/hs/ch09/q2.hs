-- Q9-2
--
--
isPalindrome text = processedText == reverse processedText
  where noSpaces = filter (\= ' ') text
        processedText = map toLower noSpaces
