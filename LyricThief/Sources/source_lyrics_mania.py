#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 21:53:29 EST 2012
# 
# 

import sys

sys.path.append('..')
sys.path.append('../Helpers')

from basic_music_url import BasicMusicUrl
from html_helper import HtmlHelper

class SourceLyricsMania(BasicMusicUrl):
    def __init__(self, artist, song):
        BasicMusicUrl.__init__(self, 'http://www.lyricsmania.com/', artist, song)

    def build_url(self):
        self.address = (self.base + self.song + '_lyrics_' +  
                       self.artist + self.extension).replace(' ', '_')

    def get_lyrics(self):
        source = self.get_address_source()
        source = source[source.index('id=\'songlyric')+20:]
        return HtmlHelper.breaks_to_nl(source[10:source.index('song_id = "";')-44].replace('\n', '').replace('\r', '')).strip()
        
if __name__ == '__main__':
    a = SourceLyricsMania('Counting Crows', 'Mr Jones')

    a.build_url()

    print a.address

    print a.get_lyrics()
