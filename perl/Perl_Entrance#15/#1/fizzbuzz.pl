#!/usr/bin/env perl
use strict;
use warnings;

for my $i (1 .. 100){
    print $i . " : ";
    if ($i % 3 == 0){
        print"Fizz";
        if ($i % 5 == 0){
            print"Buzz";
        }
    } elsif ($i % 5 == 0){
        print"Buzz";
    }
    print"\n";
}
