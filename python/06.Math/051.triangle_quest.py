# Problem: https://www.hackerrank.com/challenges/python-quest-1/problem
# Programmer: Md.Ashraful Haque
# Date: 27.04.2024

for i in range(1, int(input())):  #More than 2 lines will result in 0 score
    print(int((pow(10, i)/9)*i))