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
        self.btn_exit = self.connect_widget_by_name('btnExit', 'clicked', lambda x: gtk.main_quit())
        self.ent_artist = self.w_tree.get_widget('entArtist')
        self.ent_song = self.w_tree.get_widget('entSong')
        self.cmb_source = self.connect_widget_by_name('cmbSource', 'changed', self.change_current_source)
        self.result_buffer = gtk.TextBuffer()

        self.window.set_icon_from_file('Icons/LyricThiefIcon.png')
        self.cmb_source.set_active(0)
        self.w_tree.get_widget('txtResults').set_buffer(self.result_buffer)
        self.result_buffer.set_text('')

        for source in self.source_builder.get_names():
            self.cmb_source.append_text(source)

    def change_current_source(self, sender):
        if sender.get_active() != 0:
            self.current_source = sender.get_active_text()
        else:
            self.current_source = None

    def append_to_result(self, text):
        self.result_buffer.insert(self.result_buffer.get_end_iter(), text)

    def get_clicked(self, sender):
        if not self.fields_empty():
            self.result_buffer.set_text('')
            artist, song = self.ent_artist.get_text(), self.ent_song.get_text()
            source_found = None
            lyrics = ''

            source_names = self.source_builder.get_names() if self.current_source==None else [self.current_source] 
            for source_name in source_names:
                try:
                    source = self.source_builder.build_from_source(source_name, artist, song)
                    source.build_url()
                    lyrics = source.get_lyrics()
                    source_found = source_name
                    break
                except:
                    self.append_to_result('\n' + source_name + " failed")

            if source_found:
                self.run_lyric_window(lyrics, artist, song)
                self.append_to_result('\n\n' + source_found + ' found it!' + '\n-----------------------')
            else:
                self.append_to_result('\n\nFailed to find song\n-----------------------')

    def run_lyric_window(self, lyrics, artist, song):
        text_buffer = gtk.TextBuffer()
        lyric_window = LyricWindow(TitleHelper.capitalize_music(artist +' - ' + song))
        text_buffer.set_text(lyrics)
        lyric_window.tvi_lyrics.set_buffer(text_buffer)
        self.window.hide()
        lyric_window.window.show()
        gtk.main()
        self.window.show()
        
    def fields_empty(self):
        return self.ent_artist.get_text() == '' and self.ent_song.get_text() == ''


a = LyricThiefWindow()

a.window.show()

gtk.main()
