# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem
# Programmer: Md. Ashraful Haque
# Date: 10.08.2024

from itertools import combinations

text, k = input().split(" ")
k = int(k)

# Find all possible combinations, up to size k :1-k (included)
for i in range(1, k+1):
    # The text combinations must be sorted, so we sort before finding combinatios
    for com in combinations(sorted(text), i):
        print("".join(com))