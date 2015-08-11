#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Convert unix timestamp to date inside squid access.log

Usage:
 cat /var/log/squid/access.log | squid-accesslog.py

 echo '1439146822.083 126405 10.0.0.1 ... HIER_DIRECT/2.2.1.9 -' | squid-accesslog.py
 2015-08-10 00:00:22.083000 126405 10.0.9.1 ... HIER_DIRECT/2.2.1.9 -
'''

import sys
import datetime

if sys.argv[1] in ('-h', '--help'):
    print(__doc__)
    exit()

def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

data = sys.stdin.readlines()

for line in data:
    date = timestamp_to_date(float(line.split()[0]))
    print('{0} {1}'.format(date, line[15:]).strip())
