#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Mount all cifs shares from /etc/fstab

/etc/fstab example:
  //192.168.1.1/share /home/user/share cifs user,username=my_username,iocharset=utf8,noauto 0 0
'''

import os
import os.path
import subprocess
import sys

class MountGui:

    MOUNTCIFS = '/sbin/mount.cifs'
    ZENITY = '/usr/bin/zenity'
    drives = []
    password = ''

    def __init__(self):
        if not os.path.exists(self.MOUNTCIFS):
            exit('{0} not found. Please install cifs-utils package'.format(self.MOUNTCIFS))
        if not os.path.exists(self.ZENITY):
            exit('{0} not found. Please install zenity package'.format(self.ZENITY))

        self.drives = self.parse_fstab()

        if self.drives:
            for drive in self.drives:
                dest = drive[1]
                self.create_dir(dest)
                if self.is_mounted(dest):
                    exit(2)
        else:
            sys.exit('Cifs shares not found in /etc/fstab')

        self.password = self.get_password()

        if not self.password:
            self.notify('gtk-error', 'Пустой пароль недопустим', rc=3)

    def get_password(self):
        password = subprocess.check_output(['zenity', '--password', '--title',
            'Введите пароль']).strip()
        return password

    def parse_fstab(self):
        """Parse fstab
        Return dict: [drive[0], drive[1]], where drive[0] = source, drive[1] = destination
        """
        drives = []
        with open('/etc/fstab', 'r') as fstab:
            for line in fstab:
                if 'cifs' in line and not line.startswith('#'):
                    drive = line.strip().split()
                    drives.append(drive)
        return drives

    def create_dir(self, dir):
        """Create destination directory if does not exist"""
        if not os.path.exists(dir):
            print 'Create directory: {0}'.format(dir)
            os.mkdir(dir)

    def is_mounted(self, dir):
        """Check directory already mounted? /etc/mtab
        Return: True - mounted, False - not mounted
        """
        with open('/etc/mtab', 'r') as mtab:
            for line in mtab:
                if dir in line:
                    self.notify('gtk-info', 'Диск {0} уже подключен'.format(dir), 4)
                    return True
        return False

    def mount(self):
        """Mount drives"""
        for drive in self.drives:
            print('Mount {0}'.format(drive))
            src = drive[0]
            dest = drive[1]

            rc = subprocess.call('PASSWD="{0}" {1} {2} {3}'.format(
                self.password, self.MOUNTCIFS, src, dest), shell=True)
            if rc == 0:
                self.notify('gtk-ok', 'Диск {0} подключен успешно'.format(dest))
            else:
                self.notify('gtk-stop', 'Диск {0} не подключен'.format(dest), rc)

    def notify(self, icon, body, rc=0):
        subprocess.call(['notify-send', '-i', icon, 'Mount', body])
        print(body)
        if rc != 0:
            sys.exit(rc)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('Usage: mount-gui.py')
        print __doc__
        sys.exit(0)
    mount_gui = MountGui()
    mount_gui.mount()
