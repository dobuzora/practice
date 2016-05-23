#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 同じ文字が2回連続している行を全て表示

while(<>) {
	chomp;
	#if (/(.+)\1/) { # 私はこうして書いた!!
	if (/(\S)\1/) {
		say $_;
	}
}