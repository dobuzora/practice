#!/usr/bin/env perl
use strict;
use warnings;
use 5.010;

# 実行方法
# % perl ex6-2.pl data_6-2

# 大文字を小文字を区別しているため、And,andが別でカウントされてしまっている

my %count_word;
my @word;
# ちょっと改造して...
# オバマ大統領の演説の単語を数を数える.
while(<>){
	chomp;
	@word = split / /, $_;
	foreach (@word){
		# 正規表現で英単語のみを
		$_ =~ s/\.$//g ;
		$_ =~ s/\,$//g ;
		$_ =~ s/\:$//g ;
		$_ =~ s/\;$//g ;
		if (exists $count_word{$_}){
			$count_word{$_}++;
		} else {
			$count_word{$_} = 1;
		}
	}
}

my @sort_list;
my $num = 0;

while ((my $key,my $value) = each %count_word) {
	@sort_list[$num] = ($value . " " . $key);
	$num++;
}

@sort_list = sort { $a <=> $b } (@sort_list);
foreach (@sort_list) {
	say $_;
}