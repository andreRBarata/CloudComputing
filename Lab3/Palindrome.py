#!/usr/bin/python

import sys

#for word in sys.argv[1:]:
#  print (word[::-1] == word)

words = [
  "Oxo", "OXO", "123454321",
  "ROTATOR", "12345  54321"
]

for word in words:
  print (word[::-1] == word)