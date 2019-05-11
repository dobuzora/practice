アルゴリズムと計算量
===

## 概要

書籍にて記載されているC++のコード `maximum_profit.cpp` と計算量がO(n^2)となるアルゴリズムの `maximum_profit_slow.cpp` 、そして、Goで書いた `maximum_profit.go` を作成した。

Goの実装の方はC++のコードに寄せ、スライスではなく配列を使って書いた。

入力と最大条件となる入力は `test.py` で得る。

## How to

### Setup

```
$ make
```

### Clean

```
$ make clean
```

## Measurement

### maximum_profit.cpp
```
python3 test.py | /usr/bin/time -l ./maximum
999981269
        1.30 real         0.75 user         0.00 sys
   1589248  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
       395  page reclaims
         2  page faults
         0  swaps
         0  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
         4  voluntary context switches
       534  involuntary context switches
```

### maximum_profit_slow.cpp
```
python3 test.py | /usr/bin/time -l ./slow_maximum
999981269
      143.23 real       140.76 user         0.41 sys
   1589248  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
       397  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
         3  voluntary context switches
     73513  involuntary context switches
```

### maximum_profit.go
```
python3 test.py | /usr/bin/time -l ./go_maximum
999981269
        0.53 real         0.02 user         0.02 sys
   8536064  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
      1909  page reclaims
       190  page faults
         0  swaps
         0  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
       244  voluntary context switches
      2099  involuntary context switches
```

## まとめ

あたりまえだが、O(n^2)はO(n)と比べるとべらぼうに遅くなった。
自分で問題を解く前にプログラム読んだしまったため、自分であればどんなアルゴリズムで説いたのかは不明だが、これまでの私の場合、処理速度より先にまず問題を解くためのアルゴリズムを考えるため、速度面にも気を使わないと大変遅くなってしまうという教訓を得た。

また、予想外だったのは今回のケースはGoのほうがC++より早かったこと。