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
    parser.add_argument('-f', '--fabric', help='Output text in fabric-like hosts format (host1,host2)', action='store_true')
    parser.add_argument('-d', '--debug', help='Print raw text for debug', action='store_true')
    parser.add_argument('subnet', type=str, help='Network subnet (for example 10.1.1.0/24)')
    parser.set_defaults(func=print_output)
    return parser.parse_args()

def print_output(args):
    output = get_output(args)

    # add time to the output
    if args.time:
        print('Date: {0}'.format(datetime.now()))

    if args.fabric:
        # fabric-like output format: host1,host2,host3
        result = []
        for line in output:
            result.append(line[0])
        print(','.join(result))
    else:
        # simple output format
        for line in output:
            print('{0: <16} {1}'.format(line[0], line[1]))

def get_output(args):
    try:
        cmd = subprocess.check_output('{1} -sP -n {0}'.format(args.subnet, NMAP), stderr=subprocess.STDOUT, shell=True)
        output = re.findall('Nmap scan report for (.*)\nHost is ([up|down].*)', cmd, re.MULTILINE)
        output.sort()
        if args.debug:
            print('DEBUG: raw subprocess output')
            print(cmd)
            print('DEBUG: raw output after regex and sorting')
            print(output)
        return output
    except:
        print('Error in running {0}'.format(NMAP))
        exit(3)

if __name__ == "__main__":
    if isfile(NMAP):
        args = parse_args()
        args.func(args)
    else:
        print('{0} not found. First install nmap.'.format(NMAP))
        exit(2)
