#!/usr/bin/env perl
use strict;
use warnings;
use feature 'say';

# 数列の四則演算

my @list = ("+", "-", "*", "/","");

LAST:foreach my $ans (1000..9999) {
    my @num = split //,$ans;
    my $rev = join "",reverse @num;
    foreach my $i (@list) {
	foreach my $j (@list) {
	    foreach my $k (@list) {
		if ($i eq "" && $j eq "" && $k eq ""){
		    next;
		}
		my $line = "$num[0]$i$num[1]$j$num[2]$k$num[3]";
		#say $line;
		#say eval $line;
		if ($rev eq eval $line) {
		    say $line;
		    last LAST;
		}
	    }
	}
    }
}
	    

