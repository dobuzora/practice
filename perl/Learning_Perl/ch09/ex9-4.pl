#!/usr/bin/env perl
use strict;
use warnings;
use 5.014;

$^I = ".bak"; # バックアップ
my $str = '## Copyright (C) 2016 by Yours Truly';

while(<>) {
	# 一行目のperlの後に改行し、文字を挿入する
	s/perl/perl\n$str/g;
	print $_;
}