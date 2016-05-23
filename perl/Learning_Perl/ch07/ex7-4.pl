#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 先頭が大文字になっている行を全て表示

while(<>) {
	chomp;
	if (/[A-Z].* /) {
		say $_;
	}
}