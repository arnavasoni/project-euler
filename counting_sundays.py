from collections import OrderedDict

months = OrderedDict( [("January",31),("February", 28),("March",31),
                       ("April", 30), ("May", 31), ("June", 30),
                       ("July", 31), ("August", 31), ("September", 30),
                       ("October", 31), ("November", 30), ("December", 31)] )

days = ['Tuesday','Wednesday', 'Thursday','Friday','Saturday', 'Sunday', 'Monday']

day = 0
sunday_count = 0

def isLeap(year): #https://en.wikipedia.org/wiki/Leap_year#Algorithm
  leap = True
  if year % 4 != 0:
     leap = False
  elif year % 100 != 0:
     leap = True
  elif year % 400 != 0:
     leap = False
  return leap

for year in range(1901,2001):
  leap = isLeap(year)

  for m in months:
      dayName = days[day%7]
      if dayName == "Sunday":
         sunday_count += 1
      #print year, m, dayName
      day += months[m]
      if leap == True and m == "February":
          day += 1

print(sunday_count)
# print 171