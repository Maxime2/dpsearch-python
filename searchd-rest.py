#!/usr/bin/python

import json
import urllib
import urllib2

url = 'http://inet-sochi.ru:7003/'

params = {
    'dt' : 'back',
# The category of the results, 09 - for australian sites
    'c' : '09',
# number of results per page, i.e. how many results will be returned
    'ps': 10,
# result page number, starting with 0
    'np' : 0,
# synonyms use flag, 1 - to use, 0 - don't
    'sy' : 0,
# word forms use flag, 1 - to use, 0 - don't (search for words in query exactly)
    'sp' : 1,
# search mode, can be 'near', 'all', 'any'
    'm' : 'near',
# results groupping by site flag, 'yes' - to group, 'no' - don't
    'GroupBySite' : 'no',
# search result template 
    'tmplt' : 'json2.htm',
# search result ordering, 'I' - importance, 'R' - relevance, 'P' - PopRank, 'D' - date; use lower case letters for descending order
    's' : 'IRPD',
# search query, should be URL-escaped
    'q' : 'careers'
}

data = urllib.urlencode(params)

full_url = url + '?' + data

result = json.load(urllib2.urlopen(full_url))

rD = result['responseData']

for res in rD['results']:
 print res['title']
 print ' => ' + res['url']
 print

print ' ** Total ' + rD['found'] + ' documents found in ' + rD['time'] + ' sec.'
print ' Displaying documents ' + rD['first'] + '-' + rD['last'] + '.'

