import json, urllib2
from settings import *

class Person(object):
  def __init__(self, **kwargs):
    # print(kwargs.keys())
    for k,v in kwargs.items():
      self.__dict__[k] = v

  def __unicode__(self):
    try:
      return self.name
    except:
      return str(self.__dict__.keys())

  def __repr__(self):
    return self.__unicode__()

  def GetInfo(self, profile = "small"):
    url = "http://api.allocine.fr/rest/v3/person?partner=%s&format=json&code=%s&profile=%s" % (PARTNER_CODE, self.code, profile)
    output = urllib2.urlopen(url).read()
    d = json.loads(output)
    for k,v in d["movie"].items():
      self.__dict__[k] = v