#!/usr/bin/env perl
use strict;
use warnings;
use 5.014;

# 環境変数ENVがよくわからなかったため、中身を表示するだけのプログラム

foreach (keys %ENV) {
	print $_ . ":"x3 . $ENV{$_} . "\n"; 
}