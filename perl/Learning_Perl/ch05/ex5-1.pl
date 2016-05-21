#!/usr/bin/env perl
use strict;
use warnings;

my @list;
while (<>) {
	 unshift(@list,$_)
}
print @list;

# こっちの方が早くて短い
# print reverse <>;