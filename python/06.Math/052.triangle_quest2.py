# Problem: https://www.hackerrank.com/challenges/python-quest-2/problem
# Programmer: Md.Ashraful Haque
# Date: 27.04.2024

for i in range(1, int(input())+1):
    print(int(((10**i - 1)//9)**2)) # Basically, 11^2=121,111^2=12321,1111^2=1234321...etc