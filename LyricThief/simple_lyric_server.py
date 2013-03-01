#!/usr/bin/env python

# Created by Michael Gilliland
# Date: 
# 
#

import sys
sys.path.append('./Sources')
sys.path.append('./Helpers')

from builder_of_sources import BuilderOfSources

class LyricServer(object):
    def __init__(self):
        self.source_builder = BuilderOfSources()
        self.artist = None
        self.song = None
        self.lyrics = None

    def try_get_lyrics(self):
        """
            Tries to get the lyrics of the current object's artist and song
        """
        source_names = self.source_builder.get_names()
        for source_name in source_names:
            try:
                source = self.source_builder.build_from_source(source_name, self.artist, self.song)
                source.build_url()
                self.lyrics = source.get_lyrics()
                break
            except:
                pass

test = True

if __name__ == '__main__' and test:
    a = LyricServer()
    a.artist = "Counting Crows"
    a.song = "Omaha"

    a.try_get_lyrics()

    print a.lyrics

elif __name__ == '__main__':
    pass # The main function will go here
