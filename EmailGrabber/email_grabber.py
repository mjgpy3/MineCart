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

class EmailFileWriter:
    def __init__(self, name):
        self.output_name = name

    def write(self, emails, output_file_name):
        raise NotImplementedError("Each writer must be able to write!")

class CsvWriter(EmailFileWriter):
    def __init__(self):
        EmailFileWriter.__init__(self, "CSV")

    def write(self, emails, output_file_name):
        with open(output_file_name, 'w') as f:
            for email in emails:
                f.write(email + ',\n')
