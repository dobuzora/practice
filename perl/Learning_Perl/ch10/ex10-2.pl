#!/usr/bin/env perl
use strict;
use warnings;
use 5.014;

# 1から100までから選んだ秘密の数をユーザに当ててもらうプログラム

my $Debug = $ENV{DEBUG} // 1;
my $answer = int(1 + rand 100);
print "secret's number is $answer\n" if $Debug;
print "1~100までの値から当たりを選んでください:";

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