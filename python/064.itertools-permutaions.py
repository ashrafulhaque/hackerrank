# Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Programmer: Md. Ashraful Haque
# Date: 10.08.2024

from itertools import permutations

text = list(input().split(" "))

permmutaion_values = sorted(permutations(text[0], int(text[1])))

for value in permmutaion_values:
    print("".join(value)) # join value[0], and value[1] by ""