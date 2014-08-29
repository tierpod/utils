#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thanks to seletskiy: https://github.com/seletskiy/pidgin-start-conv

import sys
import dbus

def get_accounts(purple):
	accounts = {}
	for acc_id in purple.PurpleAccountsGetAllActive():
		accounts[acc_id] = {
			'name': purple.PurpleAccountGetUsername(acc_id),
			'proto': purple.PurpleAccountGetProtocolName(acc_id)
		}
	return accounts

def get_buddies(purple, accounts):
	buddies = {}
	for acc_id in accounts:
		for buddy_id in purple.PurpleFindBuddies(acc_id, ''):
			if not purple.PurpleBuddyIsOnline(buddy_id):
				continue
			buddy_name = purple.PurpleBuddyGetName(buddy_id)
			buddy_alias = purple.PurpleBuddyGetAlias(buddy_id)
			buddies[buddy_name] = {
				'acc_id': acc_id,
				'name': buddy_name,
				'alias': buddy_alias
			}
	return buddies

def print_buddies(buddies):
	for buddy in buddies.values():
		print '{0}/{1}'.format(buddy['alias'].encode('utf-8'), buddy['name'])

def main():
	bus = dbus.SessionBus()
	bus_obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
	purple = dbus.Interface(bus_obj, "im.pidgin.purple.PurpleInterface")
	accounts = get_accounts(purple)

	if len(sys.argv) == 2:
		if sys.argv[1] in ('-p', '--print'):
			buddies = get_buddies(purple, accounts)
			print_buddies(buddies)
		else:
			arg = sys.argv[1]
			print arg
			if arg.find('/') == -1:
				name = arg
			else:
				name = arg.split('/')[1]
			for account in accounts:
				buddy_id = purple.PurpleFindBuddy(account, name)
				if buddy_id:
					buddy_name = purple.PurpleBuddyGetName(buddy_id)
					purple.PurpleConversationNew(1, account, buddy_name)
	else:
		print 'Usage: pidgin-start-conv.py [-p|--print] user@contact'
		print 'With dmenu: pidgin-start-conv.py "$(pidgin-start-conv.py -p | dmenu.xft -l 20 -i -fn \'UbuntuMono-12\')"'

if __name__ == '__main__':
	main()
