# Problem: https://www.hackerrank.com/challenges/py-set-union/problem
# Programmer: Md.Ashraful Haque
# Date: 21.04.2024

n_eng = int(input())
roll_eng = set(map(int, input().split()))
n_fr = int(input())
roll_fr = set(map(int, input().split()))

eng_or_fr = roll_eng.union(roll_fr)
print(len(eng_or_fr))