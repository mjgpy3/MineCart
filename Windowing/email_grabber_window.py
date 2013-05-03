#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Tue Jan 15 22:47:46 EST 2013
# 
# 

"""
    The window that allows the entry of URLs to read emails from.
"""

from glade_window import GladeWindow
import gtk
import sys

sys.path.append('../EmailGrabber')

import email_grabber
from email_writer import available_writers

class EmailGrabberWindow(GladeWindow):
    """
        The window that is in charge of getting a URL from the user to be
        scraped.
    """
    def __init__(self):
        GladeWindow.__init__(self, './GladeFiles/EmailGrabberWindow.glade')
        
        self.window = self.connect_widget_by_name('wdwMain',
                                                  'destroy',
                                                  lambda x: gtk.main_quit())
        self.connect_widget_by_name('btnQuit',
                                    'clicked',
                                    lambda x: gtk.main_quit())
        self.window.set_title("Email Grabber")
        self.vbx_formats = self.w_tree.get_widget("vbxFormats")
        self.txt_url = self.w_tree.get_widget('txtUrl')
        self.txt_output = self.w_tree.get_widget('txtOutput')
        self.connect_widget_by_name('btnGet', 'clicked', self.save_emails)

        first = True
        writer = None
        for writer in available_writers:
            if first:
                button = gtk.RadioButton(None, writer)
            else:
                gtk.RadioButton(button, writer)

            button.connect("toggled", self.toggled_writer, writer)
            self.vbx_formats.pack_start(button)
            first = False
        
        button.set_active(True)
        self.active_output = writer

        self.window.show_all()

    def toggled_writer(self, sender, writer):
        """
            Sets the output type
        """
        if sender.get_active():
            self.active_output = writer

    def save_emails(self, sender):
        """
            In charge of saving the file once things are done. Requires
            all other operations in the module to be done (essentially).
        """
        if self.txt_url.get_text() == "" or self.txt_output.get_text() == "":
            raise Exception("Need to enter a URL and output file name")

        emails = email_grabber.get_email_from_url(self.txt_url.get_text())
        
        writer = available_writers[self.active_output]()
        writer.write(emails, self.txt_output.get_text())

WINDOW_INSTANCE = EmailGrabberWindow()

gtk.main()
