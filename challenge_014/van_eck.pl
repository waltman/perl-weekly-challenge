#!/usr/bin/env perl
use strict;
use warnings;
use feature 'say';

my @seen;
my $val = 0;

for my $n (0..10) {
    say "$n $val";
    $val = exists $seen[$val] ? $val = $n - $seen[$val] : 0;
    $seen[$val] = $val;
}
