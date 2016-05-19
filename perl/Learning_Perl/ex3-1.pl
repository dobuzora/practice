#!/usr/bin/env perl
use strict;
use warnings;

my @string_list = <STDIN>; # 文字列リストの読み込み
@string_list = reverse @string_list; # 逆順に並び替え
print @string_list; # 表示

# print reverse <STDIN>;