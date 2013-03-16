#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Sat Nov 17 17:09:01 EST 2012
# 
# 

"""
    A class containing methods for dealing with URLs.
"""

import re

class UrlHelper:
    """
        Contains static methods for dealing with URLs.
    """
    @classmethod
    def remove_url_nonesense(cls, phrase):
        """
            Removes invalid characters that won't work in a URL.
        """
        return re.sub('[\"|\'|?|\.|\,]', '', phrase)
