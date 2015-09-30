#!/usr/bin/python

total = 0

old = 1
new = 1

count = 2

while (len(str(new)) < 1000):
  next = old + new

  if (next % 2 == 0):
    total += next

  count += 1

  old = new
  new = next

print(count)