#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

chomp(my @input = <STDIN>); # chompはここで使える！！
my $num = shift @input;
say ((1..9,0)x(($num+9) / 10));
foreach (@input){
	# chomp; # 修正前はここで処理をしていた
	printf("%${num}s\n",$_); # ${}で変数を入れられるみたい！！%dで頑張っていた...
	# printf "%*s\n",$num,$_; # (*) アスタリスクでも展開可能！！
}



