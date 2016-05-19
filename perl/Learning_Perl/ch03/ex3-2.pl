#!/usr/bin/env perl
use strict;
use warnings;

# リスト作成
my @list = qw(fred betty dino wilma pebbles bamm-bamm); 
print"文字を入力してください、終了はCtrl+Dです\n";
my @num = <STDIN>; # リスト読み込み
# 読み込んだリストから対応するインデックスのスカラーを表示
foreach my $i (@num) { 
	print $list[$i-1] . " ";
}
print "\n"; # 改行