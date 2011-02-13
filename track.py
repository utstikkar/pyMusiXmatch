#!/usr/bin/env python
"""
track.py
 by A. Anglade and T. Bertin-Mahieux
"""

import os
import sys
import time
import datetime

class Track(object):
	"""
	Class to query the musixmatch API tracks
	"""
	
	#track.get in API
	def __init__(self):
		"""
		Takes a musixmatch ID or musicbrainz id or echo nest track id
		"""
		
		self._tid = ''
		return
		
	#track.lyrics.get in API	
	def lyrics(self):
		"""
		"""
		raise NotImplementedError
		
	#track.subtitle.get	in API
	def subtitles(self):
		raise NotImplementedError
		
	#track.chart.get in API	
	def charts(self):
		raise NotImplementedError
		
		
#track.search in API		
def search():
	track_list = list()
	
	return track_list