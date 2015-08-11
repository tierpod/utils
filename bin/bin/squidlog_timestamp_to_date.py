#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Usage:
 echo '1439146822.083 126405 10.0.0.1 TCP_MISS/200 646 CONNECT ok.ru:443 username HIER_DIRECT/2.2.1.9 -' | squid.py
 2015-08-10 00:00:22.083000 126405 10.0.9.1 TCP_MISS/200 646 CONNECT ok.ru:443 username HIER_DIRECT/2.2.1.9 -
'''

import sys
import datetime

def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

data = sys.stdin.readlines()

for line in data:
    date = timestamp_to_date(float(line.split()[0])) 
    print('{0} {1}'.format(date, line[15:]).strip())
