#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 行末に空白文字がある行を全て表示する新しいプログラム

while(<>) {
	chomp;
	if (/\s\Z/){
		print $_ . '/';
	}
}