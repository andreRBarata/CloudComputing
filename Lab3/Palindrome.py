#!/usr/bin/python

import sys

for word in sys.argv[1:]:
  print (word[::-1] == word);