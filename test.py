#!/usr/bin/env python
"""
test.py
   by Amelie Anglade and Thierry Bertin-Mahieux
      amelie.anglade@gmail.com & tb2332@columbia.edu

Testing code for the pyMusixMatch wrapper.
Can serve as a demo.

(c) 2011, A. Anglade and T. Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
from musixmatch import track as TRACK
from musixmatch import artist as ARTIST
from musixmatch import tracking as TRACKING

def die_with_usage():
    """ HELP MENU """
    print 'test.py'
    print ' by A. Anglade and T. Bertin-Mahieux'
    print '    New York Music Hack Day, February 2011'
    print ''
    print 'This code test the MusixMatch Python API'
    print 'It also serves as a demo.'
    print "CAREFUL: it uses API requests, you're probably limited."
    print ''
    print 'USAGE'
    print '   python test.py -go'
    sys.exit(0)

if __name__ == '__main__':
    
    # help menu
    if len(sys.argv) < 2 or sys.argv[1] in ('help','-help','--help'):
        die_with_usage()

    # create a track
    track = TRACK.Track(4110618)
    print '*********** TRACK 4110618 ACQUIRED ************'
    print track

    # get a list of tracks from a search
    tracks = TRACK.search(q='Rick Astley Never Gonna Give You Up')
    print '********** LIST OF TRACKS ACQUIRED ************'
    for k in range(min(3,len(tracks))):
        print tracks[k]

    # get a list of tracks from charts
    tracks = TRACK.chart()
    print '****** LIST OF TRACKS FROM CHART ACQUIRED ******'
    for k in range(min(3,len(tracks))):
        print tracks[k]

    # lyrics
    lyrics_dict = track.lyrics()
    print '************* LYRICS ACQUIRED ************'
    print lyrics_dict

    # artist
    artist = ARTIST.Artist(10832)
    print '*********** ARTIST 10832 ACQUIRED ************'
    print artist

    # get a list of artists from a search
    artists = ARTIST.search(q='Jean Leloup')
    print '********** LIST OF ARTISTS ACQUIRED ************'
    for k in range(min(3,len(artists))):
        print artists[k]

    # get a list of artists from charts
    artists = ARTIST.chart()
    print '**** LIST OF ARTISTS FROM CHART ACQUIRED *******'
    for k in range(min(3,len(artists))):
        print artists[k]

    # get a base url for my domain
    base_url = TRACKING.get_tracking_url('http://myawesomewebsite.com')
    print '********** TRACKING URL BUILT ************'
    print base_url

    # get clearance rights for my song
    song_rights_url = TRACKING.rights_clearance(base_url,'Bon Jovi','Leaving on a Prayer')
    print '********** SONG CLEARANCE RIGHTS ACQUIRED ************'
    print song_rights_url
