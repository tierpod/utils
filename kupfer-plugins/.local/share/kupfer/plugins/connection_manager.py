# -*- coding: UTF-8 -*-
__kupfer_name__ = _("Connection Manager")
__description__ = _("Connect to hosts via ssh, vnc")
__version__ = "2013-04-18"
__author__ = "Pavel Podkorytov"

__kupfer_actions__ = ("ConnectSSH", "ConnectVNC")
__description__ = _("Connect to hosts via ssh, vnc")

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support

__kupfer_settings__ = plugin_support.PluginSettings(
	{
		"key" : "vnc_string",
		"label" : _("VNC connection program"),
		"type" : str,
		"value" : "vinagre",
	}
)

class ConnectSSH(Action):
	def __init__(self):
		Action.__init__(self, _("ConnectSSH"))

	def get_description(self):
		return _("Connect to host via ssh")

	def item_types(self):
		yield TextLeaf

	def activate(self, obj):
		utils.spawn_in_terminal(['ssh', str(obj)])
		#print obj

	def get_icon_name(self):
		return "terminal"

class ConnectVNC(Action):
	def __init__(self):
		self.program = (__kupfer_settings__["vnc_string"])
		Action.__init__(self, _("ConnectVNC"))

	def get_description(self):
		return _("Connect to host via "+self.program)

	def item_types(self):
		yield TextLeaf

	def activate(self, obj):
		#program = (__kupfer_settings__["vnc_string"])
		#prog_argv = utils.argv_for_commandline(self.program + " " + str(obj))
		utils.spawn_async(['/usr/bin/vinagre', str(obj)])
		#print prog_argv

	def get_icon_name(self):
		return "preferences-desktop-remote-desktop"
