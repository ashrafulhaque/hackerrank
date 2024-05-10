# Program: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# Programmer: Md.Ashraful Haque
# Date: 10.05.2024

import re
n = int(input().strip())
results = []
for _ in range(n):
    phone = input().strip()
    m = re.match(r"^[7|8|9]\d{9}$", phone)
    if (m):
        results.append("YES")
    else:
        results.append("NO")

for i in results:
    print(i)