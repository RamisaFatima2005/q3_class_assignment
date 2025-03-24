import time
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks) # Output: Number of ticks since 12:00am, January 1, 1970: 1616421603.0

# Getting current time
localtime = time.localtime(ticks)
print("Local current time:", localtime) # Output : Local current time: time.struct_time(tm_year=2021, tm_mon=3, tm_mday=22, tm_hour=14, tm_min=0, tm_sec=3, tm_wday=0, tm_yday=81, tm_isdst=0)

# Formatted time
loctime = time.asctime(time.localtime(ticks))
print("Formatted time:", loctime) # Output: Show your current date and time

# Getting Calendar for a month
import calendar
cal = calendar.month(2025, 3)
print("Calendar for March 2025:")
print(cal) # Output: Show the calendar for March 2025

# The Date Time
from datetime import date
date1 = date(2025, 3, 24)
print("Date 1:", date1) # Output: Date 1: 2025-03-24
date2 = date(2025, 3, 25)
print("Date 2:", date2) # Output: Date 2: 2025-03-25

# Date Time
import datetime

t = datetime.datetime.now()
print(t) # Output: Show your current date and time

# strftime() method = convert date to string
tm = datetime.datetime(2025, 3, 24)
print(tm.strftime("%f")) # Output: 2025-03-24 00:00:00
print(tm.strftime("%A")) # Output: Wednesday
print(tm.strftime("%B")) # Output: March
print(tm.strftime("%Y")) # Output: 2025
print(tm.strftime("%d")) # Output: 24
print(tm.strftime("%m")) # Output: 03
print(tm.strftime("%H")) # Output: 00
print(tm.strftime("%M")) # Output: 00
print(tm.strftime("%S")) # Output: 00
