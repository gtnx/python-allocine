from AllocineObject import *
import Person

class Movie(AllocineObject):

  class Participation(object):
    def __init__(self, activity, person):
      self.activity = activity
      self.person = person

  def __unicode__(self):
    try:
      return self.title
    except:
      try:
        return self.originalTitle
      except:
        return "untitled"

  def getInfo(self, profile = DEFAULT_PROFILE):
    super(Movie, self).getInfo(profile)
    if "castMember" in self.__dict__:
      castMember = []
      for i in self.castMember:
        if "person" in i:
          code = i["person"]["code"]
          i["person"].pop("code")
          p = Person.Person(code, **(i["person"]))
          castMember.append(self.Participation(i["activity"], p))
      self.castMember = castMember