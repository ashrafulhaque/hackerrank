# Problem: https://www.hackerrank.com/challenges/calendar-module/problem
# Programmer: Md.Ashraful Haque
# Date: 26.08.2024

import calendar

# input date as MM DD YYYY format and convert to int values
month, day, year = map(int, input().split(" "))

# get day of week (int) : 0 for monday
day_of_week = calendar.weekday(year, month, day)

# use week_day int to get day name and convert to upper
print(calendar.day_name[day_of_week].upper())