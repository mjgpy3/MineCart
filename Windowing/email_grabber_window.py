#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Tue Jan 15 22:47:46 EST 2013
# 
# 

from glade_window import GladeWindow
import gtk
import sys

sys.path.append('../EmailGrabber')

import email_grabber
from email_writer import available_writers

class EmailGrabberWindow(GladeWindow):
    def __init__(self):
        GladeWindow.__init__(self, './GladeFiles/EmailGrabber.glade')
        
        self.window = self.connect_widget_by_name('wdwMain', 'destroy', lambda x: gtk.main_quit())
        self.connect_widget_by_name('btnQuit', 'clicked', lambda x: gtk.main_quit())
        self.window.set_title("Email Grabber")
        self.vbx_formats = self.w_tree.get_widget("vbxFormats")
        self.txt_url = self.w_tree.get_widget('txtUrl')
        self.txt_output = self.w_tree.get_widget('txtOutput')
        self.connect_widget_by_name('btnGet', 'clicked', self.save_emails)

        first = True
        for writer in available_writers:
            button = gtk.RadioButton(None, writer) if first else gtk.RadioButton(button, writer)
            button.connect("toggled", self.toggled_writer, writer)
            self.vbx_formats.pack_start(button)
            first = False
        
        button.set_active(True)
        self.active_output = writer

        self.window.show_all()

    def toggled_writer(self, sender, writer):
        if sender.get_active():
            self.active_output = writer

    def save_emails(self, sender):
        if self.txt_url.get_text() == "" or self.txt_output.get_text() == "":
            raise Exception("Need to enter a URL and output file name")

        emails = email_grabber.get_email_from_url(self.txt_url.get_text())
        
        writer = available_writers[self.active_output]()
        writer.write(emails, self.txt_output.get_text())

a = EmailGrabberWindow()

gtk.main()
