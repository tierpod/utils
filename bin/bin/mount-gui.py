#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Mount all cifs shares from /etc/fstab

Usage:
 Add to /etc/fstab (example):
  //192.168.1.1/share /home/user/share cifs user,username=my_username,iocharset=utf8,noauto 0 0
 And run ./mount-gui.py
'''

from gi.repository import Gtk
from gi.repository import Notify
import os
import os.path
import subprocess
import sys

class Icons:

    OK = 'gtk-ok'
    CANCEL = 'gtk-cancel'
    INFO = 'gtk-info'
    AUTH = 'gtk-dialog-authentication'
    STOP = 'gtk-stop'



class MountGuiWindow(Gtk.Window):

    MOUNTCIFS = '/sbin/mount.cifs'
    SPACING = 10
    USERNAME = ''

    def __init__(self):
        self.init_notify()

        if not os.path.exists(self.MOUNTCIFS):
            self.do_notify('{0} not found. Please install cifs-utils package.'.format(self.MOUNTCIFS), Icons.CANCEL)
            sys.exit(1)

        self.DISKS = self.parse_fstab()
        for field in self.DISKS[0][2].split(','):
            if field.startswith('username='):
                self.USERNAME = field.split('=')[1]

        if self.DISKS:
            for disk in self.DISKS:
                dest = disk[1]
                self.create_dir(dest)
                if self.is_mounted(dest):
                    sys.exit(2)
        else:
            sys.exit('Cifs shares not found in /etc/fstab.')

        self.init_window()

    def init_window(self):
        # window
        Gtk.Window.__init__(self, title='Введите пароль')
        self.set_resizable(False)
        self.set_border_width(10)
        self.set_icon_name(Icons.AUTH)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

        # grid
        grid = Gtk.Grid()
        grid.set_column_spacing(self.SPACING)
        grid.set_row_spacing(self.SPACING)

        # buttons
        button_ok = Gtk.Button(stock=Icons.OK)
        button_ok.connect("clicked", self.on_button_ok_clicked)

        button_exit = Gtk.Button(stock=Icons.CANCEL)
        button_exit.connect("clicked", self.on_button_exit_clicked)

        # labels
        label_hint = Gtk.Label()
        label_hint.set_justify(Gtk.Justification.CENTER)
        label_hint.set_markup(u'<big>Введите пароль\nдля доступа к сетевым дискам</big>')

        label_username_hint = Gtk.Label(u'Пользователь:', halign=Gtk.Align.END)
        label_username_hint.set_justify(Gtk.Justification.LEFT)

        label_password_hint = Gtk.Label(u'Пароль:', halign=Gtk.Align.END)
        label_password_hint.set_justify(Gtk.Justification.LEFT)

        # image
        image = Gtk.Image()
        image.set_from_icon_name(Icons.AUTH, Gtk.IconSize.DIALOG)

        # entries
        entry_username = Gtk.Entry()
        entry_username.set_text(self.USERNAME)
        entry_username.set_sensitive(False)

        self.entry_password = Gtk.Entry()
        self.entry_password.set_visibility(False)
        self.entry_password.connect('activate', self.on_button_ok_clicked)

        # list
        list_disks = Gtk.ListStore(str, str, str)
        for disk in self.DISKS:
            list_disks.append(disk)
        treeview = Gtk.TreeView(model=list_disks)
        renderer_text_source = Gtk.CellRendererText()
        renderer_text_destination = Gtk.CellRendererText()
        renderer_text_options = Gtk.CellRendererText()

        column_source = Gtk.TreeViewColumn('Source', renderer_text_source, text=0)
        column_destination = Gtk.TreeViewColumn('Destination', renderer_text_destination, text=1)
        column_options = Gtk.TreeViewColumn('Options', renderer_text_options, text=2)
        treeview.append_column(column_source)
        treeview.append_column(column_destination)
        treeview.append_column(column_options)
        treeview.set_size_request(-1, 100)

        # expander with list
        expander = Gtk.Expander()
        expander.set_label(u'Посмотреть список сетевых дисков')
        expander.set_resize_toplevel(True)
        expander.add(treeview)

        # separator
        separator = Gtk.Separator()

        # main grid
        # top header
        grid.attach(image, 0, 1, 1, 1)
        grid.attach(label_hint, 1, 1, 1, 1)
        grid.attach(separator, 0, 2, 2, 1)
        # username and password
        grid.attach(label_username_hint, 0, 3, 1, 1)
        grid.attach(entry_username, 1, 3, 1, 1)
        grid.attach(label_password_hint, 0, 4, 1, 1)
        grid.attach(self.entry_password, 1, 4, 1, 1)
        # disks list
        grid.attach(expander, 0, 5, 2, 1)
        # buttons
        grid.attach(button_exit, 0, 6, 1, 1)
        grid.attach(button_ok, 1, 6, 1, 1)

        self.add(grid)

    def init_notify(self):
        # notifications
        notify = Notify.init('mount-gui')

    def do_error_dialog(self, message=''):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, 'MountGui')
        dialog.format_secondary_text(message)
        dialog.run()
        print(message)
        dialog.destroy()

    def on_button_ok_clicked(self, widget):
        password = self.entry_password.get_text()
        if not password:
            self.do_error_dialog(message='Пустой пароль недопустим')
        else:
            self.mount(password)

    def on_button_exit_clicked(self, widget):
        Gtk.main_quit()

    def do_notify(self, message='', icon=''):
        print(message)
        notify = Notify.Notification.new('Mount', message, icon)
        notify.show()

    def parse_fstab(self):
        """Parse fstab
        Return: [[source_drive, destination_drive, options]]
        """
        disks = []
        with open('/etc/fstab', 'r') as fstab:
            for line in fstab:
                if 'cifs' in line and not line.startswith('#'):
                    line_splitted = line.strip().split()
                    disks.append([line_splitted[0], line_splitted[1], line_splitted[3]])
        return disks

    def create_dir(self, directory):
        """Create destination directory if does not exist"""
        if not os.path.exists(directory):
            print 'Create directory: {0}'.format(directory)
            os.mkdir(directory)

    def is_mounted(self, directory):
        """Check directory already mounted? /etc/mtab
        Return: True - mounted, False - not mounted
        """
        with open('/etc/mtab', 'r') as mtab:
            for line in mtab:
                if directory in line:
                    message = 'Диск {0} уже подключен'.format(directory)
                    self.do_notify(message, Icons.INFO)
                    return True
        return False

    def mount(self, password):
        """Mount drives"""
        for disk in self.DISKS:
            print('Mount {0}'.format(disk))
            src = disk[0]
            dest = disk[1]

            cmd = 'PASSWD="{0}" {1} {2} {3}'.format(password, self.MOUNTCIFS, src, dest)
            rc = subprocess.call(cmd, shell=True)
            if rc == 0:
                self.do_notify('Диск {0} подключен успешно'.format(dest), Icons.OK)
            else:
                self.do_error_dialog(message='Ошибка при подключении диска: {0}'
                        '\n\nВозможно, введён неверный пароль'.format(dest))

        if rc == 0:
            Gtk.main_quit()



if len(sys.argv) > 1:
    print __doc__
    sys.exit(0)
win = MountGuiWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
