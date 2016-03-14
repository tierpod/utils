#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Normalize mac address to format: 'ff:ff:ff:ff:ff:ff'

Example: echo 'MAC_ADDRESS' | mac-normalize.py
'''

import sys

N = 2

if len(sys.argv) == 2:
    data = sys.argv[1].split('\n')
else:
    data = sys.stdin.readlines()

for input_line in data:
    line = input_line.lower().translate(None, ' :.-\n')
    print ':'.join([line[i:i+N] for i in range(0, len(line), N)])
