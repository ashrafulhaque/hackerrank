# Problem: https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Programmer: Md.Ashraful Haque
# Date: 27.04.2024

import re

n = int(input().strip())
result = []

for _ in range(n):
    text = input().strip()
    match = re.search(r"^[+-]?\d*\.\d+$",text)
    result.append(True if match else False)

for i in result:
    print(i)
