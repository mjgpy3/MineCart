#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 16:40:37 EST 2012
# 
# 

from url import Url
import urllib2

class BasicMusicUrl(Url):
    def __init__(self, base, artist, song, separator='-', extension='.html'):
        Url.__init__(self)

        self.base = base
        self.separator = separator
        self.extension = extension
        self.artist = artist.lower()
        self.song = song.lower()

    def build_url(self):
        raise NotImplementedError('Still must implement build_url')

    def get_lyrics(self):
        raise NotImplementedError('Must have a lyric getter')

    def get_address_source(self):
        try:
            response = urllib2.urlopen(self.address)
        except ValueError as e:
            print "Error:", e, '\nUrl (most likely) not built correctly.'
            exit()
        except urllib2.HTTPError as e:
            print "Error: Song not found"
            exit()

        return response.read()
