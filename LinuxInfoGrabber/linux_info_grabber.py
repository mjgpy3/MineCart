#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Sat Jan 19 09:58:13 EST 2013
# 
# 

"""
    Returns HTML code of various Linux System details.
"""

from os import system, popen

PACKMANS = {'Aptitude': 'which aptitude',
            'apt-get': 'which apt-get',
            'YUM': 'which yum',
            'Zypper': 'which zypper',
            'RPM': 'which rpm',
            'Synaptic': 'which synaptic',
            'Pacman': 'which pacman',
            'Dpkg': 'which dpkg',
            'Yast': 'which yast'}

BROWSERS = {'Firefox': 'which firefox',
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

LANGUAGES = {'Python': 'which python',
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
    """
        From a list of Name:command returns all names of commands that work.
    """
    return [i for i in name_command if system(name_command[i]) == 0]

def find_value(command):
    """
        Returns working commands outputs.
    """
    return [popen(i).read() for i in command if system(i) == 0]

def find_kernel():
    """
        Returns the kernel's info.
    """
    return popen('uname -r').read().split('\n')[0]

def get_distro():
    """
        Returns the distro's name
    """
    try:
        with open('/etc/issue', 'r') as fstream:
            return fstream.read().split('\n')[0]
    except IOError:
        pass

def has_command(command):
    """
        Checks to see if a command exists on a system
    """
    return system('which ' + command) == 0

def start_table(file_stream):
    """
        Writes the beginning of a HTML table
    """
    file_stream.write('<table>\n')

def end_table(file_stream):
    """
        Writes the end of a HTML table
    """
    file_stream.write('</table>\n')

def add_row(file_stream, bold, details):
    """
        Writes a table row given the passed details
    """
    file_stream.write('  <tr>' + btd(bold+':') + ntd(details) + '</tr>\n')

def get_row(bold, details):
    """
        Returns the HTML code for a row with the passed details
    """
    return '  <tr>' + btd(bold+':') + ntd(details) + '</tr>\n'

def ntd(item):
    """
        Returns a normal table data cell
    """
    return '<td>' + str(item) + '</td>'

def btd(item):
    """
        Returns a bold table data cell
    """
    return '<td><b>' + item + '</b></td>'  

def get_html():
    """
        Returns the HTML information about the Linux system
    """
    return '<table>\n' +\
    get_row('Distro Name', get_distro()) +\
    get_row('Kernel', find_kernel()) +\
    get_row('Package Managers', ', '.join(find_key(PACKMANS))) +\
    get_row('Languages/Compliers', ', '.join(find_key(LANGUAGES))) +\
    get_row('Web Broswer(s)', ', '.join(find_key(BROWSERS))) +\
    get_row('Has sudo', has_command('sudo')) +\
    '</table>\n'

def main():
    """
        Writes a HTML file of the System's info
    """
    distro = get_distro()

    file_stream = open(distro.replace(' ', '_').replace('\\', '') +\
                                                        '.html', 'w')

    start_table(file_stream)

    add_row(file_stream, 'Distro Name', distro)
    add_row(file_stream, 'Kernel', find_kernel())
    add_row(file_stream, 'Package Managers', ', '.join(find_key(PACKMANS)))
    add_row(file_stream, 'Languages/Compliers', ', '.join(find_key(LANGUAGES)))
    add_row(file_stream, 'Web Broswer(s)', ', '.join(find_key(BROWSERS)))
    add_row(file_stream, 'Has sudo', has_command('sudo'))

    end_table(file_stream)

if __name__ == '__main__':
    main()
