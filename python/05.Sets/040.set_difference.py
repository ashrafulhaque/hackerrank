# Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Programmer: Md.Ashraful Haque
# Date: 21.04.2024

n_eng = int(input())
roll_eng = set(map(int, input().split()))
n_fr = int(input())
roll_fr = set(map(int, input().split()))

only_eng = roll_eng.difference(roll_fr)
print(len(only_eng))