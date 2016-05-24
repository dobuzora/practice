#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 文字aで終わるワードを$1にキャプチャする

while(<>) {
	chomp;
	if (/(\w+a)(\s|\Z)/){
		print "Matched : |$'<$&>$' |\n";
		print "\$1 contains \'$1\'\n"
	} else {
		print "No match : |$_|\n";
	}
}