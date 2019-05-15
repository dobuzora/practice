初等的整列
===

## 挿入ソート

書籍のコード `insertion_sort.c` と Go で書いた `insertion_sort.go` を作成した。
問題はトレースしている状態を出力するというものであったが、ソート時間の計測のためトレース部分はコメントアウトした。

書籍中にデータが降順であればO(n^2)であるが、データが昇順ならおおよそn回とあったためこれを検証する。
(ふつーに整列済みだから並び替えが発生しないからn回)

### insert_sort.c

昇順のとき

```
$ python3 test.py | /usr/bin/time ./insertion
        0.07 real         0.00 user         0.00 sys
```

降順のとき

```
$ python3 test.py -r | /usr/bin/time ./insertion
        0.20 real         0.14 user         0.00 sys
```

### insert_sort.go

昇順のとき
```
$ python3 test.py | /usr/bin/time ./go-insertion
        0.09 real         0.00 user         0.00 sys
```
降順のとき

```
$ python3 test.py -r | /usr/bin/time ./go-insertion
        0.11 real         0.04 user         0.00 sys
```

### まとめ

きちんと理論通りの結果が得られた。ただ、C++よりもGoのほうが降順ソートは早いという結果が得られたが、与える数を増やすとC++はできるのにGoでは実行できないくなった。原因の調査をしたい気持ちは大きかったがいつまで経っても先に進めないのでここでは保留にした。

## バブルソート

書籍のコード `bubble_sort.cpp` と Go で書いた `bubble_sort.go` を作成した。
計算量の大きさを比較しやすくするため、それぞれ入力数の上限を変更している。

