#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 名前付きキャプチャを使うようにする

while(<>) {
	chomp;
	if (/(?<name>\w+a)(\s|\Z)/) { # (かなり手間取った)
		print "Matched : |$'<$&>$' | \n";
		print "\'name\' contains \'$+{name}\'\n";
	} else {
		print "No match : |$_|\n";
	}
}