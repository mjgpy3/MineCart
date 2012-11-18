#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Nov 16 18:19:07 EST 2012
# 
# 

from source_azlyrics import SourceAzlyrics
from source_lyric_depot import SourceLyricDepot
from source_lyrics_mania import SourceLyricsMania

class BuilderOfSources:
    def __init__(self):
        self.sources = {'azlyrics': SourceAzlyrics, 'lyricdepot': SourceLyricDepot,
                        'lyricsmania': SourceLyricsMania}

    def get_names(self):
        return list(self.sources)

    def build_from_source(self, source_name, artist, song):
        if source_name in self.sources:
            return self.sources[source_name](artist, song)
        else:
            raise Exception('Source cannot be built!')


if __name__ == '__main__':
    b = BuilderOfSources()

    print b.get_names()

    s = b.build_from_source('lyricdepot', 'Counting Crows', 'Omaha')

    s.build_url()
    print s.get_lyrics()
