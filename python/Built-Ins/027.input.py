# Problem: https://www.hackerrank.com/challenges/input/problem
# Programmer: Md. Ashraful Haque
# Date: 19.04.2024

x, k = map(int, input().split())

poly = input()
poly.replace('x', str(x))

result = eval(poly)
print(k == result)
