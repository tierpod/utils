#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import exists
from os import mkdir
from sys import exit
from subprocess import call, check_output, CalledProcessError

def check_dir(dir):
	"""Already mounted? /etc/mtab
	Return: True - mounted, False - not mounted
	"""
	if not exists(dir): mkdir(dir)
	with open('/etc/mtab', 'r') as mtab:
		for line in mtab:
			if dir in line:
				return True
	return False

def mount_dir(pwd, src, dst):
	"""Mount drives
	Exit codes: 32 - mount error
	"""
	returncode = call('PASSWD={0} mount.cifs {1} {2}'.format(pwd, src, dst), shell=True)
	if returncode == 0:
		call("notify-send -i 'gtk-ok' 'Mount' 'Диск {0} подключен успешно'".format(dst), shell=True)
		return True
	else:
		call("notify-send -i 'gtk-stop' 'Mount' 'Диск {0} не подключен'".format(dst), shell=True)
		exit(32)

def parse_fstab():
	"""Show fstab
	Return array: drive[0] - source, drive[1] - destination
	"""
	drives = []
	with open('/etc/fstab', 'r') as fstab:
		for line in fstab:
			if 'cifs' in line and not line.startswith('#'):
			#if 'cifs' in line:
				drive = line.strip().split()
				drives.append(drive)
	return drives

def main():
	"""Parse fstab, enter password, mount drives"""
	drives = parse_fstab()
	pwd = ''
	if drives:
		for drive in drives:
			if not check_dir(drive[1]):
				if not pwd:
					try:
						pwd = check_output("zenity --password --title 'Введите пароль'", shell=True).strip()
					except CalledProcessError:
						exit(1)
				mount_dir(pwd, drive[0], drive[1])
			else:
				call("notify-send -i 'gtk-info' 'Mount' 'Диск уже подключен'", shell=True)
				exit(2)
	else:
		call("notify-send -i 'gtk-info' 'Mount' 'Не настроен /etc/fstab'", shell=True)
		exit(0)

if __name__ == "__main__":
	main()
