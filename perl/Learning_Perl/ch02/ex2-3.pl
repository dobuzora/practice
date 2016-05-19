#!/usr/bin/env perl
use strict;
use warnings;
use Math::Trig;

print"ぷろんぷと > ";
my $radius = <STDIN>; # 読み込み

# 読み込んだ値が負なら0を出力する
if ($radius >= 0) {
	print 2 * $radius * pi . "\n";
	} else {
		print"0\n";
	}