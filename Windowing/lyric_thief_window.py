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
from title_helper import TitleHelper
from builder_of_sources import BuilderOfSources


class LyricThiefWindow(GladeWindow):
    def __init__(self):
        GladeWindow.__init__(self, './GladeFiles/LyricThiefWindow.glade')
        
        self.source_builder = BuilderOfSources()        
        self.current_source = None

        self.window = self.connect_widget_by_name('wdwMain', 'destroy', lambda x: gtk.main_quit())
        self.btn_get = self.connect_widget_by_name('btnGet', 'clicked', self.get_clicked)
        self.btn_save = self.connect_widget_by_name('btnSave', 'clicked', self.save_clicked)
        self.ent_artist = self.w_tree.get_widget('entArtist')
        self.ent_song = self.w_tree.get_widget('entSong')
        self.cmb_source = self.connect_widget_by_name('cmbSource', 'changed', self.change_current_source)

        self.cmb_source.set_active(0)

        for source in self.source_builder.get_names():
            self.cmb_source.append_text(source)

    def change_current_source(self, sender):
        if sender.get_active != 0:
            self.current_source = sender.get_active_text()
        else:
            self.current_source = None

    def get_clicked(self, sender):
        if not self.fields_empty():
            artist, song = self.ent_artist.get_text(), self.ent_song.get_text()
            lyric_window = LyricWindow(TitleHelper.capitalize_music(artist +' - ' + song))
            text_buffer = gtk.TextBuffer()
            if self.current_source:
                source = self.source_builder.build_from_source(self.current_source ,artist, song)
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
