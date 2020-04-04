checkEven n = if isEven
              then n - 2
              else 3 * n + 1
              where 
                isEven = even n
