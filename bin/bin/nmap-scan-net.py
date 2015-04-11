#!/usr/bin/python

from datetime import datetime
from os.path import isfile
from sys import exit
import argparse
import subprocess, re

NMAP='/usr/bin/nmap'

def parse_args():
    parser = argparse.ArgumentParser(description='Network scanner', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-t', '--time', help='Add time to the output', action='store_true')
    parser.add_argument('subnet', type=str, help='Network subnet (for example 10.1.1.0/24)')
    parser.set_defaults(func=print_output)
    return parser.parse_args()

def print_output(args):
    output = get_output(args)
    if args.time:
        print 'Date: {0}'.format(datetime.now())
    for line in output:
        print '{0} {1}'.format(line[0], line[1])

def get_output(args):
    try:
        cmd = subprocess.check_output('{1} -sP {0}'.format(args.subnet, NMAP), stderr=subprocess.STDOUT, shell=True)
        output = re.findall('Nmap scan report for (.*)\n(Host is [up|down].*)\..*', cmd, re.MULTILINE)
        output.sort()
        return output
    except:
        return 'Error in running {0}'.format(NMAP)
        exit(3)

if __name__ == "__main__":
    if isfile(NMAP):
        args = parse_args()
        args.func(args)
    else:
        print('{0} not found. First install nmap.'.format(NMAP))
        exit(2)
