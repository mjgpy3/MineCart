#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Tue Nov 13 15:13:19 EST 2012
# 
# 

import pygtk
pygtk.require('2.0')
import gtk
import sys
sys.path.append('../LyricThief/Sources/')
sys.path.append('../LyricThief/')
sys.path.append('../LyricThief/Helpers/')

from glade_window import GladeWindow
from lyric_window import LyricWindow
from source_lyric_depot import SourceLyricDepot
from title_helper import TitleHelper


class LyricThiefWindow(GladeWindow):
    def __init__(self):
        GladeWindow.__init__(self, './GladeFiles/LyricThiefWindow.glade')
        self.window = self.connect_widget_by_name('wdwMain', 'destroy', lambda x: gtk.main_quit())
        self.btn_get = self.connect_widget_by_name('btnGet', 'clicked', self.get_clicked)
        self.btn_save = self.connect_widget_by_name('btnSave', 'clicked', self.save_clicked)
        self.ent_artist = self.w_tree.get_widget('entArtist')
        self.ent_song = self.w_tree.get_widget('entSong')

    def get_clicked(self, sender):
        if not self.fields_empty():
            artist, song = self.ent_artist.get_text(), self.ent_song.get_text()
            lyric_window = LyricWindow(TitleHelper.capitalize_music(artist +' - ' + song))
            text_buffer = gtk.TextBuffer()
            source = SourceLyricDepot(artist, song)
            source.build_url()

            text_buffer.set_text(source.get_lyrics())
            lyric_window.tvi_lyrics.set_buffer(text_buffer)
            self.window.hide()
            lyric_window.window.show()
            gtk.main()
            self.window.show()

    def save_clicked(self, sender):
        print "Clicked save"

    def fields_empty(self):
        return self.ent_artist.get_text() == '' and self.ent_song.get_text() == ''


a = LyricThiefWindow()

a.window.show()

gtk.main()
