#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 21:53:29 EST 2012
# 
# 

import sys

sys.path += ['..', '../Helpers']

from basic_music_url import BasicMusicUrl
from html_helper import HtmlHelper

class SourceLyricDepot(BasicMusicUrl):
    def __init__(self, artist, song):
        BasicMusicUrl.__init__(self, 'http://www.lyricsdepot.com/', artist, song)

    def build_url(self):
        self.address = (self.base + self.artist.replace(' ', '-') + '/' + 
                       self.song.replace(' ', '-') + self.extension)

    def get_lyrics(self):
        source = self.get_address_source()
        source = source[source.index('ringmatch')+18:]
        return HtmlHelper.breaks_to_nl(source[10:source.index('ringmatch')-37])
        

a = SourceLyricDepot('Counting Crows', 'Mr Jones')

a.build_url()

print a.get_lyrics()
