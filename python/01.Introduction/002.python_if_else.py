# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Programmer: Md. Ashraful Haque
# Date: 22.03.2024

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n in range(2,6):
    print("Not Weird")
elif n in range(6,21):
    print("Weird")
elif n > 20:
    print("Not Weird")
