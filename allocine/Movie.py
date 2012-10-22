from AllocineObject import *

class Movie(AllocineObject):
  def __unicode__(self):
    try:
      return self.title
    except:
      try:
        return self.originalTitle
      except:
        return "untitled"
