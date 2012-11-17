#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 16:40:37 EST 2012
# 
# 

from url import Url
import urllib2
import sys
sys.path.append('./Helpers')

from url_helper import UrlHelper

class BasicMusicUrl(Url):
    def __init__(self, base, artist, song, separator='-', extension='.html'):
        Url.__init__(self)

        self.base = base
        self.separator = separator
        self.extension = extension
        self.artist = UrlHelper.remove_url_nonesense(artist.lower())
        self.song = UrlHelper.remove_url_nonesense(song.lower())

    def build_url(self):
        raise NotImplementedError('Still must implement build_url')

    def get_lyrics(self):
        raise NotImplementedError('Must have a lyric getter')

    def get_address_source(self):
        try:
            response = urllib2.urlopen(self.address)
        except ValueError as e:
            raise Exception("Error:" + str(e) + '\nUrl (most likely) not built correctly.')
        except urllib2.HTTPError as e:
            raise Exception('Urlllib Error.')
        except Exception:
            raise Exception('Unheard of exception occured')

        return response.read()
