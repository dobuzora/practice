#!/usr/bin/env perl
use strict;
use warnings;
use 5.014;

# Fredを全てWilmaに変え、Wlilmaを全てFredに変える

# 唯一のコマンドライン引数をチェック
my $in = $ARGV[0];
if (! defined $in) {
	die "Usage: $0 filename";
}

# output用のファイル名を決める
my $out = $in;
$out =~ s/(\.\w+)?$/.out/;

# ハンドルチェック
if (! open $in_fh,'<',$in) {
	die "Can't open '$in': $!";
}
if (! open $out_fh,'>',$out){
	die "Can't write '$out': $!";
}

# 処理
while(<$in_fh>) {
	# これだと正常に動作しない
	# s/Fred/Wilma/gi;
	# s/Wilma/Fred/gi;
	chomp;
	s/Fred/\n/gi; # ブレースホルダーを使う
	s/Wilma/Fred/gi;
	s/\n/Fred/g; 
	print $out_fh $_;
}