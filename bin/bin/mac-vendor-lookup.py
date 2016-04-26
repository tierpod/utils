#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://www.macvendorlookup.com/mac-address-api
'''

import json
import requests
import sys

if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
    print 'Usage: mac-vendor-lookup.py 00:00:00:00:00:00'
    exit(1)

API_URL = 'https://www.macvendorlookup.com/api/v2'
URL = '%s/%s' % (API_URL, sys.argv[1])

print 'Request url: %s' % URL
r = requests.get(URL)
print json.dumps(json.loads(r.text), indent=4)
