#/usr/bin/env perl
use strict;
use warnings;

print"Please input Strings >";
my $str = <STDIN>; # 文字列読み込み

print"Please input Number > ";
my $num = <STDIN>; # 数値読み込み

# 入力値が0になる前までループを回す
while ($num > 0) {
	print $str;
	$num--;
}