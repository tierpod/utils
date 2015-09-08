#!/usr/bin/gawk -f
# http://wiki.squid-cache.org/SquidFaq/SquidLogs

{
	$1=strftime("%F.%H:%M:%S", $1);
	print $0;
}
