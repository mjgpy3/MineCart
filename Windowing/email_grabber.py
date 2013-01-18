#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Tue Jan 15 22:47:46 EST 2013
# 
# 

from glade_window import GladeWindow
import gtk

class EmailGrabberWindow(GladeWindow):
    def __init__(self):
        GladeWindow.__init__(self, './GladeFiles/EmailGrabber.glade')
        
        self.window = self.connect_widget_by_name('wdwMain', 'destroy', lambda x: gtk.main_quit())
        self.connect_widget_by_name('btnQuit', 'clicked', lambda x: gtk.main_quit())
        self.window.set_title("Email Grabber")
        self.vbxFormats = self.w_tree.get_widget("vbxFormats")

        self.window.show_all()


a = EmailGrabberWindow()

gtk.main()
