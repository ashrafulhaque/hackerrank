# Problem: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Programmer: Md.Ashraful Haque
# Date: 30.08.2024

import re

n = int(input())

for _ in range(n):
    s = input()
    try:
        pattern = re.compile(s)
        print("True")        
    except re.error:
        print("False")