#!/usr/bin/env perl
use strict;
use warnings;
use 5.014;

# ファイル名を一斉に書き換えるプログラム

# ファイル名が1 ~ のようになっていることが前提である
# 今後の追加要素として、ファイルの作成日を取得して自動的にソートしてくれるとなお良い

for(glob "*.png") { # リネームする拡張子を指定
	my $old_name =  $_;
	s/([0-9][0-9])\.png/src01_re$1\.png/;
	my $new_name = $_;
	rename $old_name, $new_name;
}
