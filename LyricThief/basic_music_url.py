#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 16:40:37 EST 2012
# 
# 

import url

class BasicMusicUrl(url.Url):
    def __init__(self, base='', separator='-', extension='.html', artist='', song=''):
        url.Url.__init__(self)

        self.base = base
        self.separator = separator
        self.extension = extension
        self.artist = artist.lower()
        self.song = song.lower()


