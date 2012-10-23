from AllocineObject import *
import Movie

class Person(AllocineObject):
  
  class Participation(object):
    def __init__(self, activity, movie):
      self.activity = activity
      self.movie = movie

  def __unicode__(self):
    if "name" in self.__dict__:
      if isinstance(self.name, unicode):
        return self.name
      elif "given" in self.name and "family" in self.name:
        return "%s %s" % (self.name["given"], self.name["family"])
      elif "given" in self.name:
        return self.name["given"]
      elif "family" in self.name:
        return self.name["family"]
      else:
        return str(self.__dict__.keys())
    else:
      return str(self.__dict__.keys())

  def getFilmography(self, profile = DEFAULT_PROFILE):
    url = "http://api.allocine.fr/rest/v3/filmography?partner=%s&code=%s&format=json&profile=%s" % (PARTNER_CODE, self.code, profile)
    output = urllib2.urlopen(url).read()
    d = json.loads(output)["person"]["participation"]
    self.__dict__["filmography"] = []
    for i in d:
      if "movie" in i:
        code = i["movie"]["code"]
        i["movie"].pop("code")
        m = Movie.Movie(code, **(i["movie"]))
        self.__dict__["filmography"].append(self.Participation(i["activity"], m))

    # return d