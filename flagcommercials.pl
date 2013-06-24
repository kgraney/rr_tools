#!/usr/bin/perl

use strict;
use warnings;

my $dir = '/var/lib/mythtv/recordings/';

opendir(DIR, $dir) or die $!;

while (my $file = readdir(DIR)) {
	# Use a regular expression to ignore files beginning with a period
	if ($file =~ m/\.mpg$/) {
		my $newfile = $file;
		$newfile =~ s/\.mpg/\.txt/g;
		if( -e $dir . $newfile ) {
			print "Do Nothing\n";
		} else {
			print "Perform commercial detection on $file\n";
			#`/usr/bin/comskip --ini=/var/tmp/comskip-0.93c/comskip.ini -q $dir$file `;
			`/usr/bin/comskip -q $dir$file `;
		}
	}

}

closedir(DIR);
exit 0;

