"""
TODO
"""

MUSIXMATCH_API_KEY = None

import os

if('MUSIXMATCH_API_KEY' in os.environ):
    MUSIXMATCH_API_KEY = os.environ['MUSIXMATCH_API_KEY']
else:
	#TODO change that?
    MUSIXMATCH_API_KEY = None

API_HOST = 'developer.musixmatch.com/'

def call(method, params):
	#TODO check API key and JSON
    for k,v in params.items():
        if isinstance(v, unicode):
            params[k] = v.encode('utf-8')
    params = urllib.urlencode(params)
    
    url = 'http://%s%s?%s' % (API_HOST, method, params)
    f = urllib.urlopen(url)
    response = f.read()
    return check_status(response)

def check_status(etree):
	#
    code = int(etree._children[0]._children[0].text)
    message = etree._children[0]._children[1].text
    if code!=0:
        raise MusiXmatchAPIError(code, message)
    else:
        return etree