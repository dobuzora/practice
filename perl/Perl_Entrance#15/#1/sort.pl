#!/usr/bin/env perl
use strict;
use warnings;

my @array = (0,0,0);
for my $i (0 .. ($#array)){
    $array[$i] = <STDIN>;
    chomp $array[$i];
}

my @sorted = sort {$a cmp $b} @array;

for my $j (0 .. ($#array)){
    print $array[$j] . "\n";
}
