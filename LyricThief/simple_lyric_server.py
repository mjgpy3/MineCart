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
        self.result

    def try_get_lyrics(self):
        source_names = self.source_builder.get_names() if self.current_source==None else [self.current_source]
        for source_name in source_names:
            try:
                source = self.source_builder.build_from_source(source_name, artist, song)
                source.build_url()
                lyrics = source.get_lyrics()
                source_found = source_name
                break
            except:
                self.append_to_result('\n' + source_name + " failed")

    def append_to_result(self, text):
        self.result_buffer.insert(self.result_buffer.get_end_iter(), text)


