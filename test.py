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
import track as TRACK




def die_with_usage():
    """ HELP MENU """
    print 'test.py'
    print ' by A. Anglande and T. Bertin-Mahieux'
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
