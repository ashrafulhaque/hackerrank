# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Programmer: Md.Ashraful Haque
# Date: 23.08.2024

from collections import defaultdict

n, m = map(int, input().split(" "))

group_a = []
group_b = []

# input values for group a in sepetared lines
for _ in range(n):
    group_a.append(input())

# input values for group b in sepetared lines
for _ in range(m):
    group_b.append(input())

result_dict = defaultdict()

for b in group_b:
    if b in group_a:
        # list com. containing list of indexes for repetition of a value of group_b
        result_dict[b] = [index+1 for index, value in enumerate(group_a) if value == b]
        # prints a list of str values in one line, space separeted
        print(" ".join(map(str,result_dict[b])))    
    else:
        print(-1)

