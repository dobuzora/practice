#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 挨拶をするサブルーチン
sub greet {
	state @name; # stateを使う ( use 5.010がないと使えない？ )
	push(@name,@_);
	if (@name == 1){
		print "Hi $name[0]! You are the first one here!\n";
	} else {
		print "Hi $name[1]! $name[0] is also here!\n";
	}
}

greet("Fred");
greet("Barney");