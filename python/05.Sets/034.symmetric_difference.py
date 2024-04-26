# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Programmer: Md.Ashraful Haque
# Date: 20.04.2024

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

result = set()

result.update(a.difference(b))
result.update(b.difference(a))

result = sorted(result)
for i in result:
    print(i)