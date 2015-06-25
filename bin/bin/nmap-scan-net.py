#!/usr/bin/python

from datetime import datetime
from os.path import isfile
from sys import exit
import argparse
import subprocess
import json

NMAP='/usr/bin/nmap'

def parse_args():
    parser = argparse.ArgumentParser(description='Network scanner',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-t', '--time', action='store_true',
        help='Add time to the output')
    parser.add_argument('-o', '--output', default='default',
        choices=['fabric', 'json', 'default'],
        help='Output format: fabric, json, default')
    parser.add_argument('-d', '--debug', action='store_true',
        help='Print raw text for debug')
    parser.add_argument('subnet', type=str,
        help='Network subnet (for example 10.1.1.0/24)')
    parser.set_defaults(func=print_output)
    return parser.parse_args()

def print_output(args):
    output = get_output(args)

    if args.time:
        print output.split('\n')[0]

    if args.output == 'json':
        result = {}
        for line in output.split('\n'):
            if line.startswith('Host'):
                _line = line.split()
                result[_line[1]] = {}
                result[_line[1]]['hostname'] = _line[2].translate(None, '()')
                result[_line[1]]['status'] = _line[4]
        print json.dumps(result, indent=4)
    elif args.output == 'fabric':
        result = []
        for line in output.split('\n'):
            if line.startswith('Host'):
                _line = line.split()
                result.append(_line[1])
        print(','.join(result))
    else:
        for line in output.split('\n'):
            if line.startswith('Host'):
                _line = line.split()
                print '{0: <16} {1: <16}'.format(_line[1], _line[2].translate(None, '()'))

def get_output(args):
    try:
        output = subprocess.check_output('{1} -sP {0} -oG -'.format(
            args.subnet, NMAP), stderr=subprocess.STDOUT, shell=True)
    except:
        print('Error in running {0}'.format(NMAP))
        exit(3)

    if args.debug:
        print('DEBUG: raw output after regex and sorting')
        print(output)
    return output

if __name__ == "__main__":
    if isfile(NMAP):
        args = parse_args()
        args.func(args)
    else:
        print('{0} not found. First install nmap.'.format(NMAP))
        exit(2)
