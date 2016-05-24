#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 文字aで終わるワードの直後に続く最大5文字を別のキャプチャ変数にキャプチャし表示

while(<>) {
	chomp;
	if (/(?<name>\b\w+a\b)(?<second>.{0,5})/){ # (途中からごり押し)
		print "Matched : |$'<$&>$' |\n";
		print "\'name\' contains \'$+{name}\'\n";
		print "\'second\' contains \'$+{second}\'\n";
	} else {
		print "No match : |$_|\n";
	}
}