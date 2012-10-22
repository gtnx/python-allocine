import urllib, urllib2, json
from settings import *
from Movie import Movie
from Person import Person
from Review import Review


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

  def reviewList(self, movie_code):
    d = json.loads(urllib.urlopen("http://api.allocine.fr/rest/v3/reviewlist?partner=%s&format=json&code=%s" % (PARTNER_CODE, movie_code)).read())
    return [Review(**i) for i in d["feed"]["review"]]