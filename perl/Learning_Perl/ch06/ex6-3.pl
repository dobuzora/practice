#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

my @key = sort keys %ENV; # ENVのキーをソートして取得
printf "%-30s%s\n",$_,$ENV{$_} for @key;　# 後置のfor