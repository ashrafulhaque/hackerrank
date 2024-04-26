# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Programmer: Md.Ashraful Haque
# Date: 26.04.2024

set_a = set(map(int, input().strip().split()))
n = int(input().strip())
results = []

for _ in range(n):
    other_set = set(map(int, input().strip().split()))
    # better way to find difference of lengths between to sets
    diff = len(other_set - set_a)
    if (set_a.issuperset(other_set) and diff == 0):
        results.append(True)
    else:
        results.append(False)
# using format() method and list comprehension to shape output
print("{result}".format(result=False if False in results else True))