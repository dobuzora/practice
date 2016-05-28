#!/usr/bin/env perl
use strict;
use warnings;
use 5.014;

# 1から100までから選んだ秘密の数をユーザに当ててもらうプログラム

print "1~100までの値から当たりを選んでください:";
my $answer = int(1 + rand 100);
while (1){
	chomp(my $input = <STDIN>);
	# 終了条件
	if ($input eq 'exit' || $input eq 'quit' || ! $input) { 
		say "終了します";
		last;
	} elsif ($answer == $input) {
		say "正解！！おめでとう！！";
		last;
	} else {
		my $hinto = ($answer > $input) ? "too small" : "too big";
		say $hinto;
	}

}