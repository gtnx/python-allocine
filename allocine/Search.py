import urllib, urllib2, json
from settings import *
from Movie import Movie
from Person import Person


class Search(object):
  class SearchResults(object):
    def __init__(self, d):
      print(d.keys())
      self.movies = [Movie(**i) for i in d.get("movie",[])]
      self.persons = [Person(**i) for i in d.get("person",[])]

  def __init__(self):
    pass

  def search(self, qry, count = 10):
    url = "http://api.allocine.fr/rest/v3/search?partner=%s&format=json&q=%s&count=%s" % (PARTNER_CODE, urllib.quote_plus(qry), count)
    d = json.loads(urllib2.urlopen(url).read())
    return self.SearchResults(d["feed"])
