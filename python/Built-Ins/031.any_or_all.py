# Problem: https://www.hackerrank.com/challenges/any-or-all/problem
# Programmer: Md.Ashraful Haque
# Date: 19.04.2024

n = int(input())
li = list(map(int, input().split()))
print(all([x>0 for x in li]) and any([str(n) == str(n)[::-1] for n in li]))