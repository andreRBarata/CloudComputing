#!/usr/bin/python

import datetime

startdate = datetime.date(1901, 1, 1)
enddate = datetime.date(2000, 12, 31)
curdate = startdate

sundaycount = 0

while (curdate < enddate):
  if (curdate.day == 1):
    sundaycount += 1

  curdate += datetime.timedelta(days=7)

print(sundaycount)