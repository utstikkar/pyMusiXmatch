"""
util.py
   by Amelie Anglade and Thierry Bertin-Mahieux
      amelie.anglade@gmail.com & tb2332@columbia.edu

Set of util functions used by the MusixMatch Python API,
mostly do to HMTL calls.

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
import copy
import urllib
try:
    from Queue import PriorityQueue, Empty
except ImportError:
    from queue import PriorityQueue, Empty
try:
    import json
except ImportError:
    import simplejson as json

# MusixMatch API key, should be an environment variable
MUSIXMATCH_API_KEY = None
if('MUSIXMATCH_API_KEY' in os.environ):
    MUSIXMATCH_API_KEY = os.environ['MUSIXMATCH_API_KEY']

# details of the website to call
API_HOST = 'api.musixmatch.com'
API_SELECTOR = '/ws/1.1/'

# cache time length (seconds)
CACHE_TLENGTH = 3600

class TimedCache():
    """
    Class to cach hashable object for a given time length
    """
    def __init__(self):
        """ contructor, init main dict and priority queue """
        self.stuff = {}
        self.queue = PriorityQueue()
        
    def cache(self,query,res):
        """
        Cache a query with a given result
        Use the occasion to remove one old stuff if needed
        """
        # remove old object
        try:
            old_obj = self.queue.get_nowait()
            t = time.time()
            if t - old_obj[0] > CACHE_TLENGTH:
                # object could actually have been changed for newer
                if t - self.stuff[old_obj[1]][0] > CACHE_TLENGTH:
                    self.stuff.pop(old_obj[1])
                if t - old_data[0] < CACHE_TLENTH
            else:
                self.queue.put_nowait(old_obj)
        except Empty:
            pass
        # add object to cache
        try:
            # I ASSUME IT'S NOT IN THERE
            hashcode = hash(query)
            self.stuff[hashcode] = (time.time(), copy.deepcopy(res))
            self.queue.put_nowait( (time.time() , hashcode ) )
        except TypeError,e:
            print 'Error, stuff not hashable:',e
            pass
        
    def query_cache(self,query):
        """
        query the cache for a given query
        Return None if not there or too old
        """
        hashcode = hash(query)
        if hashcode in self.stuff.keys():
            data = self.stuff[hashcode]
            if time.time() - data[0] > CACHE_TLENGTH:
                self.stuff.pop(data[1])
                return None
            return data[1]
        return None
        

# typical API error message
class MusixMatchAPIError(Exception):
    """
    Error raised when the status code returned by
    the MusixMatch API is not 200
    """
    def __init__(self, code, message):
        self.args = ('MusixMatch API Error %d: %s' % (code, message),)


def call(method, params):
    """
    Do the GET call to the MusixMatch API
    """
    for k,v in params.items():
        if isinstance(v, unicode):
            params[k] = v.encode('utf-8')
    # sanity checks
    params['format']='json'
    if not 'apikey' in params.keys() or params['apikey'] is None:
        params['apikey'] = MUSIXMATCH_API_KEY
    if params['apikey'] is None:
        raise MusixMatchAPIError(-1,'EMPTY API KEY')
    # encode the url request, call
    params = urllib.urlencode(params)
    url = 'http://%s%s%s?%s' % (API_HOST, API_SELECTOR, method, params)
    print url
    f = urllib.urlopen(url)
    response = f.read()
    # decode response into json
    response = decode_json(response)
    # return body if status is OK
    return check_status(response)

def decode_json(raw_json):
    """
    Transform the json into a python dictionary
    or raise a ValueError
    """
    try:
        response_dict = json.loads(raw_json)
    except ValueError:
        raise MusixMatchAPIError(-1, "Unknown error.")
    return response_dict

def check_status(response):
    """
    Checks the response in JSON format
    Raise an error, or returns the body of the message
    RETURN:
       body of the message in JSON
       except if error was raised
    """
    if not 'message' in response.keys():
        raise MusixMatchAPIError(-1,'Unknown error')
    msg = response['message']
    if not 'header' in msg.keys():
        raise MusixMatchAPIError(-1,'Unknown error')
    header = msg['header']
    if not 'status_code' in header.keys():
        raise MusixMatchAPIError(-1,'Unknown error')
    code = header['status_code']
    if code != 200:
        raise MusixMatchAPIError(code,'(code description to be implemented)')
    # all good, return body
    body = msg['body']
    return body
