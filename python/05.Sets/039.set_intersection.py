# Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation
# Programmer: Md.Ashraful Haque
# Date: 21.04.2024

n_eng = int(input())
roll_eng = set(map(int, input().split()))
n_fr = int(input())
roll_fr = set(map(int, input().split()))

eng_and_fr = roll_eng.intersection(roll_fr)
print(len(eng_and_fr))