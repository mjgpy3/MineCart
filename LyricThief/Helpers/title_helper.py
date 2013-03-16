#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Nov 16 12:42:51 EST 2012
# 
# 

"""
    Contains helpers for dealing with the titles of things (songs,
    bands, etc...)
"""

class TitleHelper:
    """
        Contains static methods for dealing with titles
    """
    not_allowed = ['for', 'and', 'nor', 'but',
                   'or', 'yet', 'so', 'in', 'to',
                   'over', 'an', 'a']
    @classmethod
    def capitalize_music(cls, title):
        """
            Capitalized titles, ignores those in `not_allowed`
        """
        return ' '.join([i.capitalize() if (not i in cls.not_allowed)
                                        else i 
                                        for i in title.split(' ')])

if __name__ == '__main__':
    print TitleHelper.capitalize_music('micahel james in Gilliland - something')
        
