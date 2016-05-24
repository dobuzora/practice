#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# matchにマッチするパターン

while(<>) {
	chomp;
	if (/match/){
		print "Matched : |$'<$&>$' |\n";
	} else {
		print "No match : |$_|\n";
	}
}