#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Sat Jan 19 12:07:23 EST 2013
# 
# 

"""
   The UI used to grab some basic info about the linux system used
"""

from glade_window import GladeWindow
import gtk
import sys

sys.path.append('../LinuxInfoGrabber')

from linux_info_grabber import get_html

class LinuxInfoGrabberWindow(GladeWindow):
    """
        Gets and shows information about the linux system it's run on
    """
    def __init__(self):
        GladeWindow.__init__(self, './GladeFiles/LinuxInfoGrabberWindow.glade')

        self.text_buffer = gtk.TextBuffer()
        self.text_buffer.set_text(get_html())

        self.tvi_info = self.w_tree.get_widget('tviInfo')
        self.window = self.connect_widget_by_name('wdwMain',
                                                  'destroy',
                                                  lambda x: gtk.main_quit())

        self.tvi_info.set_buffer(self.text_buffer)

        self.window.show_all()

if __name__ == '__main__':
    MAIN_WINDOW = LinuxInfoGrabberWindow()

    gtk.main()
