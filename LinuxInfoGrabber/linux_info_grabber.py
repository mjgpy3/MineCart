#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Sat Jan 19 09:58:13 EST 2013
# 
# 

from os import system, popen

"""
    A dict of available package managers {key: value} = {Manager name: command to find}
"""
packmans = {'Aptitude': 'which aptitude',
            'apt-get': 'which apt-get',
            'YUM': 'which yum',
            'Zypper': 'which zypper',
            'RPM': 'which rpm',
            'Synaptic': 'which synaptic',
            'Pacman': 'which pacman',
            'Dpkg': 'which dpkg',
            'Yast': 'which yast'}

"""
    A dict of browsers on the OS {key: value} = {Browser name: command to find}
"""
browsers = {'Firefox': 'which firefox',
            'Chromium': 'which chromium-browser',
            'Lynx': 'which lynx', 
            'Amaya': 'which amaya',
            'Epiphany': 'which epiphany-browser',
            'Konqueror': 'which konqueror',
            'Dillo': 'which dillo',
            'Arora': 'which arora',
            'Ice Weasel': 'which iceweasel',
            'Midori': 'which modori',
            'Dooble': 'which dooble',
            'SeaMonkey': 'which seamonkey'}

languages = {'Python': 'which python',
             'Gcc (C)': 'which gcc',
             'C++': 'which c++',
             'C#': 'which csharp',
             'Ruby': 'which ruby',
             'Perl': 'which perl',
             'Haskell': 'which ghc',
             'PHP': 'which php',
             'Java': 'which javac',
             'SmallTalk': 'which gst',
             'BASH': 'which bash',
             'Fortran': 'which gfortran'}

def find_key(name_command):
    return [i for i in name_command if system(name_command[i]) == 0]

def find_value(command):
    return [popen(i).read() for i in command if system(i) == 0]

def find_kernel():
    return popen('uname -r').read().split('\n')[0]

def get_distro():
    try:
        with open('/etc/issue', 'r') as f:
          return f.read().split('\n')[0]
    except IOError:
          pass

def has_command(command):
    return system('which ' + command) == 0

def start_table(f):
    f.write('<table>\n')

def end_table(f):
    f.write('</table>\n')

def add_row(f, bold, details):
    f.write('  <tr>' + btd(bold+':') + td(details) + '</tr>\n')

def get_row(bold, details):
    return '  <tr>' + btd(bold+':') + td(details) + '</tr>\n'

def td(item):
    return '<td>' + str(item) + '</td>'

def btd(item):
    return '<td><b>' + item + '</b></td>'  

def get_html():
    return '<table>\n' +\
    get_row('Distro Name', get_distro()) +\
    get_row('Kernel', find_kernel()) +\
    get_row('Package Managers', ', '.join(find_key(packmans))) +\
    get_row('Languages/Compliers', ', '.join(find_key(languages))) +\
    get_row('Web Broswer(s)', ', '.join(find_key(browsers))) +\
    get_row('Has sudo', has_command('sudo')) +\
    '</table>\n'

if __name__ == '__main__':
   distro = get_distro()

   f = open(distro.replace(' ', '_').replace('\\', '') + '.html', 'w')

   start_table(f)

   add_row(f, 'Distro Name', distro)
   add_row(f, 'Kernel', find_kernel())
   add_row(f, 'Package Managers', ', '.join(find_key(packmans)))
   add_row(f, 'Languages/Compliers', ', '.join(find_key(languages)))
   add_row(f, 'Web Broswer(s)', ', '.join(find_key(browsers)))
   add_row(f, 'Has sudo', has_command('sudo'))

   end_table(f)

