#!/usr/bin/env perl
use strict;
use warnings;

# 平均値を計算するサブルーチン
sub calc_average {
	my $avarage = 0;
	foreach my $n (@_) {
		$avarage += $n;
	}
	return $avarage / @_;
}

# 平均より大きい値を返すサブルーチン
sub above_average {
	my $avarage = &calc_average(@_);
	my @r_list;
	foreach my $n (@_) {
		if ($n > $avarage){
			push (@r_list,$n);
		}
	}
	return @r_list;
}

my @fred = above_average(1..10);
print "\@fred is @fred\n";
print "(Should be 6 7 8 9 10)\n";
my @barney = above_average(100, 1..10);
print "\@barney is @barney\n";
print "(Should be just 100)\n";