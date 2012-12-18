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
    def __init__(self, title): 
        GladeWindow.__init__(self, './GladeFiles/LyricWindow.glade')
        self.output_file = None
        self.title = title
    
        self.tvi_lyrics = self.w_tree.get_widget('tviLyrics')
        self.window = self.connect_widget_by_name('wdwMain', 'destroy', lambda x: gtk.main_quit())
        self.window.set_title(self.title)
        self.window.set_icon_from_file('Icons/LyricThiefIcon.png')

        menu_bar = self.w_tree.get_widget('menBar')

        file_tab = gtk.MenuItem('_File')
        file_tab.show()

        sub_menu = gtk.Menu()

        for option_name in ['_Save', 'Save _As...', '_Exit']:
            item = gtk.MenuItem(option_name)
            sub_menu.append(item)
            item.connect('activate', self.file_activated, option_name)
            item.show()

        file_tab.set_submenu(sub_menu)
        sub_menu.show()
        
        menu_bar.append(file_tab)
        self.window.show()

    def file_activated(self, sender, name):
        if name == '_Exit':
            gtk.main_quit()
            self.window.hide()
        elif name == "_Save" and self.output_file == None:
            self.save_as(sender)
        elif name == "_Save" and self.output_file:
            self.save_existing(sender)
        elif name == "Save _As...":
            self.save_as(sender)

    def save_existing(self, sender):
        txt_buffer = self.tvi_lyrics.get_buffer()
        start = txt_buffer.get_start_iter()
        end = txt_buffer.get_end_iter()

        with open(self.output_file, 'w') as f:
            f.write(txt_buffer.get_text(start, end))

    def save_as(self, sender):
        chooser = gtk.FileChooserDialog(title='Save As...', action=gtk.FILE_CHOOSER_ACTION_SAVE,
                                        buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        chooser.set_icon_from_file('Icons/LyricThiefIcon.png')
        chooser.set_current_name(self.title+'.txt')
        chooser.set_default_response(gtk.RESPONSE_OK)
        a_filter = gtk.FileFilter()
        a_filter.set_name('Text File')
        a_filter.add_pattern("*.txt")
        chooser.add_filter(a_filter)

        response = chooser.run()

        if response == gtk.RESPONSE_OK:
            self.output_file = chooser.get_filename()
            self.save_existing(sender)
        chooser.destroy() 
