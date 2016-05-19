#!/usr/bin/env perl
use strict;
use warnings;

print"Please input number\n";
my $num1 = <STDIN>; # 読み込み1
my $num2 = <STDIN>; # 読み込み2

print $num1 * $num2 . "\n"; # 計算