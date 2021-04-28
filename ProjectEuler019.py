#Project Euler, Problem 19
#Counting Sundays

"""You are given the following information, but you may prefer to do some research for yourself.
        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import time
from datetime import date

def sundays(start,end):
    sundays = 0
    for year in range(start,end+1):
        for month in range(1,13):
            if date(year,month,1).weekday() == 6:
                sundays += 1
    return sundays

start = time.time()
print(sundays(1901,2000))
print(time.time() - start)
#171 in 0.000997781753540039 secs