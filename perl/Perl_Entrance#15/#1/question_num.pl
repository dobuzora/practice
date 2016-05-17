#!/usr/bin/env perl
use strict;
use warnings;

my $answer = 1;

print"数字を入力してください==>";
my $num = <STDIN>;
chomp $num;
if ($num == $answer){
    print"OK\n";
} elsif ($answer - 5 < $num && $num < $answer + 5 ){
    print"near\n"
} elsif ($num > $answer){
    print"too big\n";
} elsif ($num < $answer){
    print"too small\n";
}

