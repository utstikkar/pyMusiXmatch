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
	def __init__(self):
		"""
		Takes a musixmatch ID or musicbrainz id or echo nest track id
		"""
		
		self._tid = ''
		return
		
		
	def lyrics(self):
		"""
		"""
		raise NotImplementedError
		
	def subtitles(self):
		raise NotImplementedError
		
		
	def charts(self):
		raise NotImplementedError