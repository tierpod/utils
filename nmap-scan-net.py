#!/usr/bin/python

from datetime import datetime
import sys, subprocess, re
import argparse

def main():
	parser = argparse.ArgumentParser(description='Network scanner', formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-t', '--time', help='Add time to the output', action='store_true')
	parser.add_argument('subnet', type=str, help='Network subnet (for example 10.1.1.0/24)')
	parser.set_defaults(func=get_output)

	args = parser.parse_args()
	result = args.func(args)
	if args.time:
		print datetime.now()
	for item in result:
		print '{0} {1}'.format(item[0], item[1])
	if args.time:
		print "\n"

def get_output(args):
	try:
		cmd = subprocess.check_output('nmap -sP {0}'.format(args.subnet), stderr=subprocess.STDOUT, shell=True)
		arr = re.findall('Nmap scan report for (.*)\n(Host is [up|down].*)\..*', cmd, re.MULTILINE)
		arr.sort()
		return arr
	except:
		return "Error in running cmd"

if __name__ == "__main__":
	main()
