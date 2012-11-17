#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Sat Nov 17 17:09:01 EST 2012
# 
# 

import re

class UrlHelper:
    @classmethod
    def remove_url_nonesense(cls, phrase):
        return re.sub('[\"|\'|?|\.|\,]', '', phrase)
