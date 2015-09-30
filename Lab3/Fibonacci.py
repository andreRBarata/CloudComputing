#!/usr/bin/python

old = 1
new = 1

count = 2

while (len(str(new)) < 1000):
  next = old + new
  
  count += 1

  old = new
  new = next

print(count)