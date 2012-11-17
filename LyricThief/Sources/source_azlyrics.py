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

class SourceAzlyrics(BasicMusicUrl):
    def __init__(self, artist, song):
        BasicMusicUrl.__init__(self, 'http://www.azlyrics.com/lyrics/', artist, song, '')

    def build_url(self):
        self.address = self.base + self.artist.replace(' ', '') + '/' + self.song.replace(' ', '') + self.extension

    def get_lyrics(self):
        source = self.get_address_source()
        source = source[source.index('<!-- start of lyrics -->')+16:]
        return HtmlHelper.breaks_to_nl(source[10:source.index('<!-- end of lyrics -->')]).strip().replace('\n\n', '\n')
        
if __name__ == '__main__':
    a = SourceAzlyrics('Counting Crows', 'Mr Jones')

    a.build_url()

    print a.address

    print a.get_lyrics()
