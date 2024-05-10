# Program: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# Programmer: Md.Ashraful Haque
# Date: 10.05.2024

import re

n = int(input().strip())
txt = ""
for _ in range(n):
    txt += input() + "\n"

patterns = ["(?<=\s)&&(?=\s)", "(?<=\s)\|\|(?=\s)"]
replacements = ["and", "or"]

for patt, replace in zip(patterns, replacements):
    # replace '&&' by 'and', replace '||' by 'or'
    txt = re.sub(rf"({patt})", replace, txt)

print(txt)
