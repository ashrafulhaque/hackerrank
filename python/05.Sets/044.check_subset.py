# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
# Programmer: Md.Ashraful Haque
# Date: 26.04.2024

test_cases = int(input().strip())
results = []
for _ in range(test_cases):
    na = int(input().strip())
    set_a = set(map(int, input().split()))
    nb = int(input().strip())
    set_b = set(map(int, input().split()))
    results.append(set_a.issubset(set_b))

for i in results:
    print(i)