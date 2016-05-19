#!/usr/bin/env perl
use strict;
use warnings;
use Math::Trig;

print"ぷろんぷと > ";
my $radius = <STDIN>; # プロンプトからの読み込み

print 2 * $radius * pi . "\n"; # 計算
