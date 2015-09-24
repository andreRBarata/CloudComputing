#!/usr/bin/python

total = 0

old = 1
new = 1

while (old < 4000000 ):
  next = old + new

  if (next % 2 == 0):
    total += next

  old = new
  new = next

print(total)