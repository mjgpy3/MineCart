#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Nov 16 12:42:51 EST 2012
# 
# 

class TitleHelper:
    not_allowed = ['for', 'and', 'nor', 'but',
                   'or', 'yet', 'so', 'in', 'to',
                   'over', 'an', 'a']
    @classmethod
    def capitalize_music(cls, title):
       return ' '.join([i.capitalize() if (not i in cls.not_allowed)
                                       else i 
                                       for i in title.split(' ')])

if __name__ == '__main__':
    print TitleHelper.capitalize_music('micahel james in Gilliland - something')
        
