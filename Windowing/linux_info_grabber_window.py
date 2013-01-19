#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Sat Jan 19 12:07:23 EST 2013
# 
# 

from glade_window import GladeWindow
import gtk
import sys

sys.path.append('../LinuxInfoGrabber')

from linux_info_grabber import get_html

class LinuxInfoGrabberWindow(GladeWindow):
    def __init__(self):
        GladeWindow.__init__(self, './GladeFiles/LinuxInfoGrabberWindow.glade')

        self.text_buffer = gtk.TextBuffer()
        self.text_buffer.set_text(get_html())

        self.tvi_info = self.w_tree.get_widget('tviInfo')
        self.window = self.connect_widget_by_name('wdwMain', 'destroy', lambda x: gtk.main_quit())

        self.tvi_info.set_buffer(self.text_buffer)

        self.window.show_all()

if __name__ == '__main__':
    main_window = LinuxInfoGrabberWindow()

    gtk.main()
