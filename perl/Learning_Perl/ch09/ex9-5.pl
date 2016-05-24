#!/usr/bin/env perl
use strict;
use warnings;
use 5.014;

# コピーライト表記を2度追加されてしまうのを避ける
# 最後までわからなかった...

# 読み込むファイル名をハッシュで取得
my %do_these;
foreach (@ARGV) {
	$do_these{$_} = 1;
}

# マッチする場合はそのARGVを削除
while(<>) {
	if (/\A## Copyright/) {
		delete $do_these{$ARGV};
	}
}

@ARGV = sort keys %do_these; # 読み込むべきファイルを取得
if (!@ARGV) {
	say "行うべき処理はありません";
	exit;
}

$^I = ".bak"; # バックアップ
my $str = '## Copyright (C) 2016 by Yours Truly';

while(<>) {
	if (/\A#!/) {
		$_ .= $str . "\n";
	}
	print $_;
}

