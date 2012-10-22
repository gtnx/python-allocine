from AllocineObject import *

class Person(AllocineObject):
  def __unicode__(self):
    try:
      return self.name
    except:
      return str(self.__dict__.keys())

