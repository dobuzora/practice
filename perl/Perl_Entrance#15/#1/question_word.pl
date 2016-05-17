#!/usr/bin/env perl
use strict;
use warnings;

my $answer = 'python';

print'文字を入力してください ->';
my$str = <STDIN>;
chomp $str;
if ($str eq $answer){
    print"OK";
} else {
    print"NG";
}
