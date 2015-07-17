#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Video downloader for http://igra-prestoloff.biz/
'''

import re
import requests
import shlex
import subprocess
import sys

WGET = '/usr/bin/wget'

def main():
    directory = sys.argv[1]
    url = sys.argv[2]
    content = get_content(url)
    urls = find_urls(content)
    for _url in urls:
        download_file(_url, directory)

def get_content(url):
    print('Get content for url {0}'.format(url))
    request = requests.get(url)
    return request.text

def find_urls(content, quality='480p'):
    print('Get urls from content with quality {0}'.format(quality))
    urls = re.findall('file:"(.*{quality}.*)"'.format(**locals()), content)
    return urls

def download_file(url, directory):
    print('Download file {0} to {1}'.format(url, directory))
    try:
        subprocess.call(shlex.split('{0} -P {1} {2}'.format(WGET, directory, url)))
    except KeyboardInterrupt:
        print('\nAbord downloading')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: download-got.py /output/directory http://url/season1')
    else:
        main()
