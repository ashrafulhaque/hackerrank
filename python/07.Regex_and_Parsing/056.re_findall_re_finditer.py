# Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# Programmer: Md.Ashraful Haque
# Date: 10.05.2024

import re

text = input().strip()
matches = re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNM])[AEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNM])",text,re.IGNORECASE)
for i in matches:
    print(i)
if not matches:
    print(-1)

# *** Things to Understand: ****
# (?<=[Q..M]) is a positive lookbehind assertion, ensures that the match is preceded by a consonant character 
# [AEIOU]{2,} matches two or more consecutive vowels in case-insensitive manner (due to the re.IGNORECASE flag)
# (?=...): This is a positive lookahead assertion. It guarantees that the match is followed by another consonant character.