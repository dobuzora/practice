#!/usr/bin/env perl
use strict;
use warnings;
use feature "say";

# 10進数で回文

sub check {
    my $c = shift;
    my $rev = reverse split //,$c;
    if ($c == $rev) {
	return 1;
    } else {
	return 0;
    }
}

foreach (10..1000000) {
    if (check($_) && check(sprintf "%b" ,$_) && check(sprintf "%o",$_)){
	say "Answer is $_";
	last;
    }
}

