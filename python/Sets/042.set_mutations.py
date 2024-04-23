# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Programmer: Md.Ashraful Haque
# Date: 22.04.2024

na = int(input())
a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    cmd, m = input().split()
    b = set(map(int, input().split()))
    if cmd == "update":
        a.update(b)
    elif cmd == "intersection_update":
        a.intersection_update(b)
    elif cmd == "difference_update":
        a.difference_update(b)
    elif cmd == "symmetric_difference_update":
        a.symmetric_difference_update(b)
        
print(sum(a))