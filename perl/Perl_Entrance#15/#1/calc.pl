#!/usr/bin/env perl
use strict;
use warnings;

my $first = <STDIN>;
my $second = <STDIN>;

print $first + $second . "\n";
print $first - $second . "\n";
print $first * $second . "\n";
print $first / $second . "\n";

my $hoge = 'hello';
if ($hoge eq 'hello'){
    print"OK";
}else {
    print'NG';
}


