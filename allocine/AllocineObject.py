import json, urllib2
from settings import *

class AllocineObject(object):
  def __init__(self, **kwargs):
    for k,v in kwargs.items():
      self.__dict__[k] = v

  def __repr__(self):
    return self.__unicode__()

  def GetInfo(self, profile = "small"):
    url = "http://api.allocine.fr/rest/v3/%s?partner=%s&format=json&code=%s&profile=%s" % (self.__class__.__name__.lower(), PARTNER_CODE, self.code, profile)
    output = urllib2.urlopen(url).read()
    d = json.loads(output)
    for k,v in d["movie"].items():
      self.__dict__[k] = v