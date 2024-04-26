# Problem: https://www.hackerrank.com/challenges/py-set-add/problem
# Programmer: Md.Ashraful Haque
# Date: 21.04.2024

country_stamps = set()

n = int(input().strip())
for _ in range(n):
    country_stamps.add(input().strip())

print(len(country_stamps))