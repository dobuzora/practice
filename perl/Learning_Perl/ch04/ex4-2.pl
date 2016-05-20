#!/usr/bin/env perl
use strict;
use warnings;

sub total {
	my $sum = 0;
	foreach my $n (@_){
		$sum += $n;
	}
	return $sum;
}

my $total = &total(1..1000); # 1 ~ 1000でサブルーチンを試す
print "1から1000までの和は $total です\n";