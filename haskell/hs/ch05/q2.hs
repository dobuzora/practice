-- 
-- 部分適用
flipBinalyArgs binalyFunction = (\x y -> binalyFunction y x)

binalyPartialApplication binalyFunc arg  = (\x-> binalyFunc arg x)
