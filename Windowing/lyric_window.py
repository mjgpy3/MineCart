#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Wed Nov 14 18:28:11 EST 2012
# 
# 

import pygtk
pygtk.require('2.0')
import gtk

from glade_window import GladeWindow

class LyricWindow(GladeWindow):
    def __init__(self): 
        GladeWindow.__init__(self, './GladeFiles/LyricWindow.glade')
        self.tvi_lyrics = self.w_tree.get_widget('tviLyrics')
        self.window = self.connect_widget_by_name('wdwMain', 'destroy', lambda x: gtk.main_quit())

