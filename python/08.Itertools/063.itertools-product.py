# Problem: https://www.hackerrank.com/challenges/itertools-product/problem
# Programmer: Md.Ashraful Haque
# Date: 10.08.2024

from itertools import product

list_a = [int(a) for a in input().split(" ")]
list_b = [int(b) for b in input().split(" ")]

# compute the cartesian product of list_a and list_b
product_ab = list(product(list_a,list_b))

print(*product_ab)