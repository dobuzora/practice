#!/usr/bin/env perl
use strict;
use warnings;

my @list = <STDIN>;
print"数行で出力\n";
print sort @list;

print"一行で出力\n";
chomp(@list);
@list = sort @list;
print"@list\n";