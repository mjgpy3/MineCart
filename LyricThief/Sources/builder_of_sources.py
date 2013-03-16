#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Nov 16 18:19:07 EST 2012
# 
# 

"""
    A (I believe) factory of sources. It stores strings of the sources'
    names and returns constructors of said sources when given a name.
"""

from source_azlyrics import SourceAzlyrics
from source_lyric_depot import SourceLyricDepot
from source_lyrics_mania import SourceLyricsMania
from source_mp3_lyrics import SourceMp3lyrics

class BuilderOfSources:
    """
        A factory of lyric sources. Give the name of a source, and an
        artist and a song, you get back a source.
    """
    def __init__(self):
        self.sources = {'azlyrics': SourceAzlyrics,
                        'lyricdepot': SourceLyricDepot,
                        'lyricsmania': SourceLyricsMania,
                        'mp3lyrics': SourceMp3lyrics}

    def get_names(self):
        """
            Returns a list of a dictionary of all name:constructor pairs
        """
        return list(self.sources)

    def build_from_source(self, source_name, artist, song):
        """
            When passed a correct source name, an artist name and a song name
            it returns a correct source.
        """
        if source_name in self.sources:
            return self.sources[source_name](artist, song)
        else:
            raise Exception('Source cannot be built!')

def use_case():
    """
        A simple example of a use-case
    """
    builder = BuilderOfSources()

    print builder.get_names()

    source = builder.build_from_source('lyricdepot', 'Counting Crows', 'Omaha')

    source.build_url()
    print source.get_lyrics()

if __name__ == '__main__':
    use_case()
