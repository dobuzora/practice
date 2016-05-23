#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# ピリオドを含む行のみを表示

while(<>) {
	chomp;
	if (/\./) {
		say $_;
	}
}