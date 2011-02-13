"""
track.py
   by Amelie Anglade and Thierry Bertin-Mahieux
      amelie.anglade@gmail.com & tb2332@columbia.edu

Class and functions to query MusixMatch regarding a track
(find the track, get lyrics, chart info, ...)

This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.

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
import time
import datetime
import util

class Track(object):
	"""
	Class to query the musixmatch API tracks
	If the class is constructed with a MusixMatch ID (default),
	we assume the ID exists.
	The constructor can find the track from a musicbrainz ID
	or Echo Nest track ID.
	Then, one can search for lyrics or charts.
	"""
	#track.get in API
	def __init__(self,track_id, musicbrainz=False, echonest=False,
		     trackdata=None):
		"""
		Create a Track object based on a give ID.
		If musicbrainz or echonest is True, search for the song.
		Takes a musixmatch ID or musicbrainz id or echo nest track id
		Raises an exception if the track is not found.
		INPUT
		   track_id     - track id (from whatever service)
		   musicbrainz  - set to True if track_id from musicbrainz
		   echonest     - set to True if track_id from The Echo Nest
		   trackdata    - if you already have the information about
		                  the track (after a search), bypass API call
		"""
		if musicbrainz and echonest:
			raise ValueError('Creating a Track, only musicbrainz or echonest can be true.')
		if trackdata is None:
			if musicbrainz:
				params = {'musicbrainz_id':track_id}
			elif echonest:
				params = {'echonest_track_id':track_id}
			else:
				params = {'track_id':track_id}
			# url call
			body = util.call('track.get',params)
			trackdata = body['track']
		# save result
		for k in trackdata.keys():
			self.__setattr__(k,trackdata[k])

	# track.lyrics.get in the API
	def lyrics(self):
		"""
		Get the lyrics for that track.
		RETURN
		   dictionary containing keys:
		       - 'lyrics_body'   (main data)
		       - 'lyrics_id'
		       - 'lyrics_language'
		       - 'lyrics copyright'
		       - 'pixel_tracking_url'
		       - 'script_tracking_url'
		"""
		body = util.call('track.lyrics.get',{'track_id':self.track_id})
		return body["lyrics"]
		
	#track.subtitle.get in API
	def subtitles(self):
		raise NotImplementedError
		
	#track.chart.get in API	
	def charts(self):
		raise NotImplementedError

	def __str__(self):
		""" pretty printout """
		return 'MusixMatch Track: '+str(self.__dict__)
		
#track.search in API		
def search():
	track_list = list()
	
	return track_list
