#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Mon Nov 12 23:21:49 EST 2012
# 
# 

"""
    Contains a (static) class with HTML methods.
"""

import re

class HtmlHelper:
    """
        Contains static HTML helper methods
    """
    @classmethod
    def breaks_to_nl(cls, htmlish_code):
        """
            Replaces all breaks with newlines in passed HTML code. 
        """
        regex = re.compile('<br\s*/*>')
        return re.sub(regex, '\n', htmlish_code)

