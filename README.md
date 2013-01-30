MineCart
========

A by need/want data-miner, built in Python as a pet-project.

Components
==========

LyricThief
----------
Uses various sources (each needs a URL builder and a lyric parser) to mine lyrics from the web.

Features:
 - Finds and views lyrics by artist and song name
 - Ability to save lyrics as a txt file
 - Can use a remedial CLI interface or a spiffy GUI
 - Multiple sources can be selected using the GUI

Installation:
 - _linux_ - Should work on most modern Linux distros without installing new software. If not,
   use your distro's package manager to get PyGTK.
 - _Windows_ - Requirements: (1) Python 2.7 (2.6 will probably also work), PyGTK.

To run: 
 - Navigate to `/MineCart/Windowing/`
 - Run the file `lyric_thief_widow.py`

TODO:
 - Add batch job ability
 - After batch job is added, add miner for lists of songs per album

<hr>

EmailGrabber
----------
Snatches "all" (not tested conclusively) emails from the given URL.

Features:
 - Allows the user to make a text file in different formats of emails from a URL.

Installation:
 - _linux_ - Should work on most modern Linux distros without installing new software. If not,
   use your distro's package manager to get PyGTK.
 - _Windows_ - Requirements: (1) Python 2.7 (2.6 will probably also work), PyGTK.

To run: 
 - Navigate to `/MineCart/Windowing/`
 - Run the file `email_grabber_window.py`

<hr>

LinuxInfoGrabber
----------
Gets some basic info about the Linux machine it's residing on.

Features:
 - Has a GUI HTML output for easy copy-paste.

Installation:
 - Linux is required, this will not work on MAC or Windows.

To run: 
 - Navigate to `/MineCart/Windowing/`
 - Run the file `linux_info_grabber_window.py`

<hr>

Intended Tools:
 - Programming Language popularity tool:
   - TIOBE Index
   - Google hits
   - StackOverflow Tags
   - Wikipedia - List, Other info...
 - Project Euler problem snatcher

