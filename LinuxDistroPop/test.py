#!/usr/bin/env python
import re
import urllib2

reader = urllib2.urlopen('http://distrowatch.com/')
text = reader.read()

popular_distros = re.findall('phr2\"><a href=\".+\">(.+)</a>', text)
par_numbers = re.findall('<td class="phr3" title="Yesterday: \d+">(.+)<im', text)


