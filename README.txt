===========
Python Allocine
===========

Python Allocine provides a generic wrapper for Allocine API v3. Typical usage
often looks like this::

#!/usr/bin/env python

from allocine.Allocine import Allocine

results = Allocine().search("the godfather")
movie = results.movies[0]
print(movie.title)
movie.getInfo()
print(movie.synopsisShort)


What this wrapper can do
=========

This API allows you to query Allocine

* Search
* Access Person & Movies & Reviews