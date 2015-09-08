#!/bin/awk -f
# http://wiki.squid-cache.org/SquidFaq/SquidLogs

BEGIN {
	count = 0;
	size = 0;
}

$4 ~ "HIT" {
	count = count + 1;
	size = size + $5;
	$1=strftime("%F.%H:%M:%S", $1);
	print $0;
}

END {
	print "=======================================================================";
	print "The size is the amount of data delivered to the client: "size/1024/1024" MB";
	print "Count of HIT records: "count;
}
