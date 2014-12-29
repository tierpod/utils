# -*- coding: UTF-8 -*-
__kupfer_name__ = _("Clipboard Templates")
__description__ = _("Copy phrases to clipboard from ~/.config/phrases.conf")
__version__ = "2014-09-17"
__author__ = "Pavel Podkorytov"

__kupfer_actions__ = ("CopyToClipboard", )
__kupfer_sources__ = ("PhrasesSource", )
__description__ = _("Copy phrases to clipbord")

import os
import codecs
import gtk

from kupfer.objects import Action, Leaf
from kupfer.obj.grouping import ToplevelGroupingSource
from kupfer.obj.helplib import FilesystemWatchMixin

def _copy_to_clipboard(text):
    clipboard = gtk.clipboard_get()
    clipboard.wait_for_text()
    clipboard.set_text(text)
    clipboard.store()

class CopyToClipboard(Action):
    """Copy text to clipboard """
    def __init__(self):
        Action.__init__(self, _("Copy to clipboard"))

    def get_description(self):
        return _("Copy text to clipboard")

    def activate(self, leaf):
        _copy_to_clipboard(str(leaf))

    def get_icon_name(self):
        return "edit-paste-symbolic"

class Phrases(Leaf):
    """ Leaf represent phrases saved in ~/.config/phrases.conf"""

    def __init__(self, name):
        Leaf.__init__(self, name, name)

    def get_actions(self):
        yield CopyToClipboard()

    def get_icon_name(self):
        return "edit-paste"

class PhrasesSource (ToplevelGroupingSource, FilesystemWatchMixin):
    """Reads ~/.config/phrases.conf and creates leaves for the hosts found.
    """
    _home = os.path.expanduser("~/.config/")
    _config_file = "phrases.conf"
    _config_path = os.path.join(_home, _config_file)

    def __init__(self, name=_("Clipboard Phrases")):
        ToplevelGroupingSource.__init__(self, name, "phrases")

    def initialize(self):
        ToplevelGroupingSource.initialize(self)
        self.monitor_token = self.monitor_directories(self._home)

    def monitor_include_file(self, gfile):
        return gfile and gfile.get_basename() == self._config_file

    def get_items(self):
        try:
            content = codecs.open(self._config_path, "r", "UTF-8").readlines()
            for line in content:
                line = line.strip()
                yield Phrases(line)
        except EnvironmentError, exc:
            self.output_error(exc)
        except UnicodeError, exc:
            self.output_error("File %s not in expected encoding (UTF-8)" %
                    self._config_path)
            self.output_error(exc)

    def get_description(self):
        return _("Phrases as specified in ~/.config/phrases.conf")

    def get_icon_name(self):
        return "edit-paste"

    def provides(self):
        yield Phrases

