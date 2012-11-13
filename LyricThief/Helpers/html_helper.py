#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 23:21:49 EST 2012
# 
# 

import re

class HtmlHelper:
    @classmethod
    def breaks_to_nl(cls, htmlish_code):
        r = re.compile('<br\s*/*>')
        return re.sub(r, '\n', htmlish_code)

