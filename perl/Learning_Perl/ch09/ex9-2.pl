#/usr/bin/env perl
use strict;
use warnings;
use 5.014;

#$^I = ".out";
#
#while(<>) {
#	s/Fred/Larry/g;
#	print $_;
#}

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
	s/Fred/Larry/gi;
	print $out_fh $_;
}


