# Program: https://www.hackerrank.com/challenges/re-start-re-end/problem
# Programmer: Md.Ashraful Haque
# Date: 10.05.2024

import re

text = input().strip()
substring = input().strip()

# Lookahead assertion with dynamic substring for overlapping matches
pattern = rf"(?={substring})"


matches = re.finditer(pattern, text)

results = []
for match in matches:
    start = match.start()
    end = start + len(substring) - 1  # Adjust end index based on substring length
    results.append((start, end))

for i in results:
    print(i)

if not results:
    print("(-1, -1)")
