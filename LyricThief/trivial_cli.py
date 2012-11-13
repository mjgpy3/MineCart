#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 23:52:11 EST 2012
# 
# 

import sys

sys.path.append('./Sources')
sys.path.append('./Helpers')

from source_lyric_depot import SourceLyricDepot

artist = raw_input('Artist Name (e.g. Pink floyd): ')

song = raw_input('Song Name: ')

a = SourceLyricDepot(artist, song)

url = a.build_url()

lyrics = a.get_lyrics()

potential_file_name = artist.replace(' ', '_') + '-' + song.replace(' ', '_') + '.txt'

print lyrics

print '\n Would you like to save to ' + potential_file_name

if raw_input('[y/n]:').lower() == 'y':
    with open(potential_file_name, 'w') as f:
        f.write(lyrics)
