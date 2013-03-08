# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('fotopull')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('fotopull')

from fotopull_lib import Window
from fotopull.AboutFotopullDialog import AboutFotopullDialog
from fotopull.PreferencesFotopullDialog import PreferencesFotopullDialog

# See fotopull_lib.Window.py for more details about how this class works
class FotopullWindow(Window):
    __gtype_name__ = "FotopullWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(FotopullWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutFotopullDialog
        self.PreferencesDialog = PreferencesFotopullDialog

        # Code for other initialization actions should be added here.

        self.transferButton = self.builder.get_object("transferButton")
        self.settingsButton = self.builder.get_object("settingsButton")
        self.mainToolbar = self.builder.get_object("mainToolbar")

        context = self.mainToolbar.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)

    # tällä nimeämistavalla ei tarvii erikseen lisätä signaaleihin... on_<elementti>_<action>
    def on_transferButton_clicked(self, widget):
        print "da click"
        

    def on_settingsButton_clicked(self, widget):
        print "settings clicked"
