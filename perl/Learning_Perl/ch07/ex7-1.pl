#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# fredにマッチする行を全て表示

while(<>) {
	chomp;
	if (/fred/) {
		say $_;
	}
}