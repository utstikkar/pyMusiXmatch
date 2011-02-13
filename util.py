"""
util.py
   by Amelie Anglade and Thierry Bertin-Mahieux
      amelie.anglade@gmail.com & tb2332@columbia.edu

Set of util functions used by the MusixMatch Python API,
mostly do to HMTL calls.

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

MUSIXMATCH_API_KEY = None
if('MUSIXMATCH_API_KEY' in os.environ):
    MUSIXMATCH_API_KEY = os.environ['MUSIXMATCH_API_KEY']

API_HOST = 'http://developer.musixmatch.com'
API_SELECTOR = '/ws/1.1/'

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
    f = urllib.urlopen(url)
    response = f.read()
    # decode response into json

    # return body if status is OK
    return check_status(response)


def check_status(response):
    """
    Checks the response in JSON format
    Raise an error, or returns the body of the message
    RETURN:
       body of the message in JSON
       except if error was raised
    """
    if not 'message' in response.keys():
        raise MusixMatchAPIError(-1,'unknown error')
    msg = response['message']
    if not 'header' in msg.keys():
        raise MusixMatchAPIError(-1,'unknown error')
    header = msg['header']
    if not 'status_code' in header.keys():
        raise MusixMatchAPIError(-1,'unknown error')
    code = header['status_code']
    if code != 200:
        raise MusixMatchAPIError(code,'(code description to be implemented)')
    # all good, return body
    body = msg['body']
    return body
