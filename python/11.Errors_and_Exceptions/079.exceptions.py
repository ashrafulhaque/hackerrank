# Problem: https://www.hackerrank.com/challenges/exceptions/problem
# Programmer: Md.Ashraful Haque
# Date: 30.08.2024

n = int(input())

for _ in range(n):
    a, b = map(str, input().split(' '))

    try:
        print(int(a)//int(b)) # integer division by // 
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)
    