# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Programmer: Md.Ashraful Haque
# Date: 20.04.2024

# n = size of arr, m = size of a, b
n, m = map(int, input().split())

arr = list(map(int,input().split()))

a = set(map(int,input().split()))
b = set(map(int,input().split()))

# initial happiness
happiness = 0

for i in range(n):
    if arr[i] in a:
        happiness += 1
    if arr[i] in b:
        happiness -= 1

print(happiness)