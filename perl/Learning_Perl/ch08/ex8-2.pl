#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# ワードのどれかがaで終わっていたらマッチするぱたーん

while(<>) {
	chomp;
	# \wが1回以上現れて、次にa、さらに空白文字をマッチパターンとした
	if (/\w+a\s/){
	# if (/a\b) { # 解答	
		print "Matched : |$'<$&>$' |\n";
	} else {
		print "No match : |$_|\n";
	}
}