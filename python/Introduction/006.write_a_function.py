# Problem: https://www.hackerrank.com/challenges/write-a-function/problem
# Programmer: Md.Ashraful Haque
# Date: 24.03.2024

def is_leap(year):
    leap = False
    
    if (year % 4) == 0 and (year % 100) != 0:
        leap = True
    elif (year % 100) == 0 and (year % 400 == 0):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))
