#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

 # fred もしくは Fred にマッチする行を全て表示

while(<>) {
	chomp;
	if (/[Ff]red/) {
		say $_;
	}
}