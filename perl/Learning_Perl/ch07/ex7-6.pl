#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# wilma と fred の両方を含む行をすべて表示

while(<>) {
	chomp;
	if (/wilma/ and /fred/) {
		say $_;
	}
}