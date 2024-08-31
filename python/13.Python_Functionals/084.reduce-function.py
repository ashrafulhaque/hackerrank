# Problem: https://www.hackerrank.com/challenges/reduce-function/problem
# Programmer: Md. Ashraful Haque
# Date: 31.08.2024

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)