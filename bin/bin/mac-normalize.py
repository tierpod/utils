#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Normalize mac address to format: 'ff:ff:ff:ff:ff:ff'

Examples:
mac-normalize.py MAC_ADDRESS
echo 'MAC_ADDRESS' | mac-normalize.py
'''

import sys

N = 2

def mac_normalize(mac):
    raw_mac = mac.lower().translate(None, ' :.-\n')
    # check length
    if len(raw_mac) != 12:
        print 'Error: wrong input length: {0} {1}/16'.format(raw_mac, len(raw_mac))
        exit(1)
    list_mac = [raw_mac[i:i+N] for i in range(0, len(raw_mac), N)]
    # check elements in list
    for elem in list_mac:
        try:
            int(elem, 16)
        except ValueError:
            print 'Error: wrong element in mac: {0} {1}'.format(elem, raw_mac)
            exit(2)
    return ':'.join([raw_mac[i:i+N] for i in range(0, len(raw_mac), N)])


if len(sys.argv) == 2:
    data = sys.argv[1].split('\n')
    for input_line in data:
        print mac_normalize(input_line)
else:
    print __doc__.strip()

