#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 21:53:29 EST 2012
# 
# 

import sys
import re

sys.path.append('..')
sys.path.append('../Helpers')

from basic_music_url import BasicMusicUrl
from html_helper import HtmlHelper

class SourceMp3lyrics(BasicMusicUrl):
    def __init__(self, artist, song):
        BasicMusicUrl.__init__(self, 'http://www.mp3lyrics.org/', artist, song, '')

    def build_url(self):
        self.address = (self.base + self.artist[0] + '/' +
                        self.artist.replace(' ', '-') + '/' + self.song.replace(' ', '-') + '/')

    def get_lyrics(self):
        return re.sub('<.+>', '', HtmlHelper.breaks_to_nl(re.findall('class=\"nocopy\">(.+)<br><br>', self.get_address_source())[0]))
        
if __name__ == '__main__':
    a = SourceMp3lyrics('Counting Crows', 'Hard Candy')

    a.build_url()

    print a.address

    print a.get_lyrics()
