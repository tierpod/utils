#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
		print '{0} / {1}'.format(buddy['alias'].encode('utf-8'), buddy['name'])

def search_buddies(user, buddies):
	for buddy in buddies.values():
		if user in '{0} {1}'.format(buddy['name'], buddy['alias'].encode('utf-8')):
			return (buddy['acc_id'], buddy['name'])

def start_conv(purple, acc_id, name):
	purple.PurpleConversationNew(1, acc_id, name)
	
def main():
	bus = dbus.SessionBus()
	bus_obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
	purple = dbus.Interface(bus_obj, "im.pidgin.purple.PurpleInterface")

	accounts = get_accounts(purple)
	buddies = get_buddies(purple, accounts)
	print_buddies(buddies)
	#buddy = search_buddies('Крав', buddies)
	#purple.PurpleConversationNew(1, buddy[0], buddy[1])

if __name__ == '__main__':
	main()
