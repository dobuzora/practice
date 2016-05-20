#!/usr/bin/env perl
use strict;
use warnings;

# 合計を返すサブルーチン
sub total {
	my $sum = 0;
	# 受け取ったものを一つずつ取り出し足し合わせる
	foreach my $n (@_){
		$sum += $n;
	}
	return $sum;
}

# サブルーチンの動作確認コード
my @fred = qw( 1 3 5 7 9);
my $fred_total = total(@fred);
print "The total of \@fred is $fred_total.\n";
print "Enter some numbers on separate lines:";
my $user_total = total(<STDIN>);
print "The total of those numbers is $user_total.\n";