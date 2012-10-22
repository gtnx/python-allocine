import datetime
from AllocineObject import *

class Review(AllocineObject):

  def __init__(self, **kwargs):
    super(Review, self).__init__(**kwargs)
    self.creationDate = datetime.datetime.strptime(self.creationDate, "%Y-%m-%dT%H:%M:%S")

  def __unicode__(self):
    return "%s : %s..." % (self.__dict__.get("author","Unknown").encode("utf8"), self.__dict__.get("body","Unknown")[:40].encode("utf8"))

