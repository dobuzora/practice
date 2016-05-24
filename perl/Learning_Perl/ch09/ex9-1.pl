#!/usr/bin/env perl
## Copyright (C) 2016 by Yours Truly
use strict;
use warnings;
use 5.014;

# $whatに3回マッチするパターンをかけ

my $what = 'fred|neko';
my $match;
while(<>) { 
	if (/($what){3}/) {
		print $_;
	}
}                                                                             