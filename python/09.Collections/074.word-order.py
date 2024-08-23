# Problem: https://www.hackerrank.com/challenges/word-order/problem
# Programmer: Md.Ashraful Haque
# Date: 23.08.2024

import collections

n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())
    
# count occarances for each word orderedly
count_occarances = collections.Counter(words)

# output: total distinct words, number of occarances, space seperated
print(len(set(words)))
print(" ".join(map(str,count_occarances.values())))