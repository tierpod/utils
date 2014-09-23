#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from os import rename, getenv, chdir
from sys import argv

chdir(getenv('HOME')+'/.purple/')
tree = ET.parse('blist.xml')

""" Sort buddy list """
container = tree.find('blist')
def getkey(elem):
	return elem.attrib['name']

container[:] = sorted(container, key=getkey)

""" Collapse all groups """
if len(argv) == 2 and argv[1] in ('-c', '--collapse'):
	contacts = tree.findall('./blist/group/setting[@name="collapsed"]')
	for contact in contacts:
		contact.text = '1'

tree.write('blist_sorted.xml')
rename('blist.xml', 'blist.xml_bak')
rename('blist_sorted.xml', 'blist.xml')
