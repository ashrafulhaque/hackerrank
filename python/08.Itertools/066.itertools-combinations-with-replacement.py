# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Programmer: Md.Ashraful Haque
# Date: 10.08.2024

from itertools import combinations_with_replacement

text, k = input().split(" ")
k = int(k)
# Find all possible combinations of text with repeatitions for size k in sorted order
combo = combinations_with_replacement(sorted(text), k)

for i in combo:
    print("".join(i))

