#!/usr/bin/env python

# Created by Michael Gilliland
# Date: 
# 
#

import sys
sys.path.append('./Sources')
sys.path.append('./Helpers')

import socket
import json

from builder_of_sources import BuilderOfSources

class LyricServer(object):
    def __init__(self):
        self.source_builder = BuilderOfSources()
        self.artist = None
        self.song = None
        self.lyrics = None
        self._socket = socket.socket()
        self._n_requests = None

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

    def define_socket(self, port, n_requests=5):
        """
            Used to define the socket object from inputs
        """
        host = socket.gethostname()
        print "Lyric Thief Server: Hostname is %s" % str(host)
        self._socket.bind((host, port))
        self._n_requests = n_requests

    def handle_lyric_requests(self):
        self._socket.listen(self._n_requests)

        while True:
            client, address = self._socket.accept()
            print "Lyric Thief Server: Connected to %s" % str(address)

            self.lyrics = ''
            data = json.loads(client.recv(1024))
            try:
                self.artist, self.song = data['artist'], data['song']
            except KeyError:
                client.send("Invalid JSON passed")
                print "Lyric Thief Server: Invalid JSON Passed"
                client.close()
                return
                
            self.try_get_lyrics()
            client.send(self.lyrics)
            print "Lyric Thief Server: Sent Lyrics, Closing Connection"
            client.close()
       

test = False

if __name__ == '__main__' and test:
    a = LyricServer()
    a.artist = "Counting Crows"
    a.song = "Omaha"

    a.try_get_lyrics()

    print a.lyrics

elif __name__ == '__main__':
    server = LyricServer()
    server.define_socket(915, 5)
    server.handle_lyric_requests()
