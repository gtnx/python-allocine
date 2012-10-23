import json, urllib2
from settings import *

class AllocineObject(object):
  _dict = dict()

  def __new__(self, code, **kwargs):
    AllocineObject._dict.setdefault(self.__module__,{})
    if code in AllocineObject._dict[self.__module__]:
      retval = AllocineObject._dict[self.__module__][code]
      retval.__init__(code, **kwargs)
    else:
      retval = super(AllocineObject, self).__new__(self, code, **kwargs)
      AllocineObject._dict[self.__module__][code] = retval
    return retval

  def __init__(self, code, **kwargs):
    self.code = code
    for k,v in kwargs.items():
      self.__dict__[k] = v

  def __unicode__(self):
    return self.__class__.__name__

  def __repr__(self):
    return ("<%s #%s: %s>" % (self.__class__.__name__, self.code, self.__unicode__())).encode("utf8")

  def getInfo(self, profile = "small"):
    url = "http://api.allocine.fr/rest/v3/%s?partner=%s&format=json&code=%s&profile=%s" % (self.__class__.__name__.lower(), PARTNER_CODE, self.code, profile)
    output = urllib2.urlopen(url).read()
    d = json.loads(output)
    for k,v in d[self.__class__.__name__.lower()].items():
      self.__dict__[k] = v
