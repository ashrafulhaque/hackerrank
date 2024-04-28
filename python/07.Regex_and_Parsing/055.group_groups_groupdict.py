# Problem: https://www.hackerrank.com/challenges/re-group-groups/problem
# Programmer: Md.Ashraful Haque
# Date: 28.04.2024

import re

text = input().strip()
# [a-zA-Z0-9] for only alphanumeric (Since, \w includes alphanumeric and _ also)
# () for grouping the return value of re.search()
# /1 to check the same pattern
check_orrur = re.search(r"([a-zA-Z0-9])\1",text)
print(check_orrur.group(1) if check_orrur else -1)

