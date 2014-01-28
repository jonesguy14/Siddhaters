#!/usr/bin/python3
import json
import urllib.request, urllib.parse

def showsome(searchfor):
  query = urllib.parse.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read().decode("utf8")
  results = json.loads(search_results)
  data = results['responseData']
  print('Total results: %s' % data['cursor']['estimatedResultCount'])
  hits = data['results']
  print('Top %d hits:' % len(hits))
  for h in hits: link = h['url']#print(' '+h['url'])
  print('For more results, see %s' % data['cursor']['moreResultsUrl'])
  return link


user_search = input("Enter search query: ")
showsome(user_search)
