#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 16:38:05 EST 2012
# 
# 

"""
    Contains the parent class (abstract) for URLs.
"""

class Url:
    """
        The parent of the urls that will be used in sources.
    """
    def __init__(self):
        self.address = ''

    def build_url(self):
        """
            When implemented should construct the URL (string)
        """
        raise NotImplementedError("Must implement build_url, even just a pass")
