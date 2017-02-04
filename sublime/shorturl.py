#!/usr/bin/python 

import urllib2
import json
import sys
import os

url = sys.argv[len(sys.argv)-1]
shortenerURL = 'https://www.googleapis.com/urlshortener/v1/url'
longURL = json.dumps({'longUrl':url})

request = urllib2.Request(shortenerURL)
request.add_header('Content-Type','application/json')

opener = urllib2.build_opener()
output = opener.open(request,longURL).read()


doc = json.loads(output)
print output
short = doc['id']

print 'The short link %s' % short

if __name__ == '__main__':
    main()