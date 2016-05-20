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
		print "Hi $name[-1]! I've seen: @name[0..(@name - 2)]\n";
	}
}

greet("Fred");
greet("Barney");
greet("Wilma");
greet("Betty");