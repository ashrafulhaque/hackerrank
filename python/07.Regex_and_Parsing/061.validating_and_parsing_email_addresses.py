# Program: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# Programmer: Md.Ashraful Haque
# Date: 10.05.2024

import re
from email.utils import parseaddr

n = int(input().strip())
results = []

for _ in range(n):
    text = input().strip()
    parsed_addr = parseaddr(text)
    email = parsed_addr[1]
    m = re.match(r"^[A-Za-z]+[\w|.|-]*@[A-Za-z]+\.[A-Za-z]{1,3}$",email)
    if (m):
        results.append(text)

for i in results:
    print(i)