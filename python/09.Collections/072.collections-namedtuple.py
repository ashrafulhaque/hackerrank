# Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Programmer: Md.Ashraful Haque
# Date: 23.08.2024

from collections import namedtuple
n, Student = int(input()), namedtuple("Student", input())
records = [Student(*input().split()) for _ in range(n)]
print(f"{sum(int(i.MARKS) for i in records) / n:.2f}")