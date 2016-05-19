#!/usr/bin/env perl
use strict;
use warnings;

my @string_list = <STDIN>;
@string_list = reverse @string_list;
print @string_list;