#!/usr/bin/python

total = 0
number = 0

while (number < 1000):
  if (number % 5 == 0 or number % 3 == 0):
    total += number
  number+=1

print(total)
