#!/usr/bin/python

import sys

# Version using system arguments
#for word in sys.argv[1:]:
#  print (word[::-1] == word)

# Words to test
words = [
  "Oxo", "OXO", "123454321",
  "ROTATOR", "12345  54321",
  67643, 5678, 1221
]

# Tests each word
for word in words:
  print (word[::-1] == word)