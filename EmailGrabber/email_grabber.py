#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Tue Jan 15 22:22:51 EST 2013
# 
# 

import re
import urllib2

def get_email_from_url(url):
    reader = urllib2.urlopen(url)
    emails = set(re.findall('[[\w|\.]+\@\w+\.\w{3}', reader.read()))
    return emails
