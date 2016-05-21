#!/usr/bin/env perl
use strict;
use warnings;
use v5.22;

say ((1..9,0)x4);

while(<>){
	chomp($_);
	printf("%20s\n",$_);
}