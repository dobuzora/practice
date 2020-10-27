-- Q9-3
--
--

harmonic n = sum (take n seriesValues)
  where seriesPairs = zip (cycle [1.0]) [1.0,2.0,..]
        seriesValues = map (\pair -> (fst pair)/(snd pair)) seriesPairs
