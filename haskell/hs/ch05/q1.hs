ifEven myFunction x = if even x
                      then myFunction x
		      else x

inc n = n + 1
double n = n*2
square n = n^2

ifEvenInc = ifEven inc
ifEvenDouble = ifEven double
ifEvenSquare = ifEven square
