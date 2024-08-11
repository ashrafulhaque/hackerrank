# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Programmer: Md.Ashraful Haque
# Date: 11.08.2024

from itertools import combinations

# get the inputs
n = int(input())
letters = list(input().split(" "))
k = int(input())
# calculate the combination of letters, each having k characters
combo = list(combinations(letters, k)) 

# count the number of 'a' 
count = 0
for i in combo:
    if 'a' in i:
        count += 1

probability = count/len(combo)
print( probability)   