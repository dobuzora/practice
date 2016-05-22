#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# ハッシュを定義
my %sample = (
	fred => "flintstone",
	barney => "rubble",
	wilma => "flintstone"
);

# 入力
say "Please Enter name...(fred,barney,wilma)";
chomp(my $input = <STDIN>);
# 存在するなら表示する
if (exists $sample{$input}) {
	say $sample{$input};
} else {
	say "Nod find $input";
}