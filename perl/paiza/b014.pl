#!/usr/bin/env perl
use strict;
use warnings;
use Data::Dumper;
use v5.22;

# 3Dプリンタ

chomp(my ($X,$Y,$Z) = split / /,<STDIN>);

my @key_list;
my @check_list;

# 場所を管理するハッシュの生成
# 及びハッシュのキーとなる配列の生成
my %list;
foreach my $z (1..$Z){
	foreach my $x (1..$X) {
		foreach my $y (1..$Y){
			push @key_list , "$x,$y,$z";
			$list{"$x,$y,$z"} = 0;
		}
	}
}

# ブロックをの有無をハッシュに管理
MAIN:while (<>) {
	chomp;
	# "--" の場合は処理せず次のループへ
	if ($_ eq "--"){
		next MAIN;
	}
	foreach my $in (split //,$_) {
		my $key = shift(@key_list);
		$list{$key} = $in;
	}
}


my %ans;
foreach my $z (1..$Z) {
	foreach my $y (1..$Y) {
		$ans{"$z,$y"} =  0;
	}
}

foreach my $z (reverse 1..$Z) {
	foreach my $y (reverse 1..$Y) {
		push @check_list,"$z,$y";
	}
}


foreach (keys %list) {
	if (/(\d*)\,(\d*)\,(\d*)/) {
		if ($list{$_} eq '#') {
			my $key = $3 . ',' . $2;
			$ans{$key} = 1;
		}
	}
}

push @check_list,"0,0";
$ans{"0,0"} = 0;
my @answer;
my @output;
my $counter = $Z;
foreach (@check_list) {
	if (/\A(\d*)/) {
		if ($counter == $1) {
			if ($ans{$_} == 1) {
				unshift @output,'#';
			} else {
				unshift @output,'.';
			}
		} else {
			push @{$answer[$Z - $counter]},@output;
			$counter = $1;
			@output = ();
			if ($ans{$_} == 1) {
				unshift @output,'#';
			} else {
				unshift @output,'.';
			}
		}
	}
}

foreach (0..@answer-1) {
	print @{$answer[$_]};
	unless ($_ == (@answer-1)) {
		print "\n";
	}
}

