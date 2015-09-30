#!/usr/bin/python

total = 0
number = 0

#Count to 1000
while (number < 1000):
  #Increment if it is a multiple of 5 or 3
  if (number % 5 == 0 or number % 3 == 0):
    #Add to total
    total += number
    
  #Increment number
  number+=1

#Print total
print(total)
