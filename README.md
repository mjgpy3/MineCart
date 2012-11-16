MineCart
========

A by need/want data-miner, built in Python as a pet-project.

_Components_:

**LyricThief**:
Uses various sources (each needs a URL builder and a lyric parser) to mine lyrics from the web.

Features:
 - Finds and views lyrics by artist and song name
 - Ability to save lyrics as a txt file
 - Can use a remedial CLI interface or a spiffy GUI

Installation:
 - _linux_ - Should work on most modern Linux distros without installing new software. If not,
   use your distro's package manager to get PyGTK.
 - _Windows_ - Requirements: (1) Python 2.7 (2.6 will probably also work), PyGTK.

To run: 
 - Navigate to `/MineCart/Windowing/`
 - Run the file `lyric\_thief\_widow.py`

TODO:
 - Make a filter in `basic\_music\_url.py` to remove URL nonsense (e.g. '.', '?', ''')...
 - Make not crash unexpectedly
 - Add more sources
 - Add a proxy for sources
 - Tie combo box to proxy for sources
 - Add batch job ability
 - After batch job is added, add miner for lists of songs per album

<hr>
