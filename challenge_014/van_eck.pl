#!/usr/bin/env perl
use strict;
use warnings;
use feature 'say';

my @seen;
my %first;
my $val = 0;
$first{0} = 1;

for my $n (0..10) {
    say "$n $val";
    if (defined $first{$val}) {
        $val = 0;
        delete $first{$val};
    } elsif (exists $seen[$val]) {
        $val = $n - $seen[$val];
    } else {
        $first{$val} = 1;
        $val = 0;
    }
#    $val = exists $seen[$val] ? $val = $n - $seen[$val] : 0;
    $seen[$val] = $val;
}
