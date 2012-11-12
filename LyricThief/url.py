#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 16:38:05 EST 2012
# 
# 

class Url:
    def __init__(self):
        self.address = ''

    def build_url(self):
        raise NotImplementedError("Must implement build_url, even just a pass")
