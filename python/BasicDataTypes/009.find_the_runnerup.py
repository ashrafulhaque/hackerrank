# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# Programmer: Md.Ashraful Haque
# Date: 26.03.2024

n = int(input())
arr = map(int, input().split())
new_array = [] # creates a blank list
new_array = sorted(list(set(arr))) #set is used to remove duplicates
print(new_array[-2])

"""
Sample Input: 
5
2 3 6 6 5
Sample Output:
5
"""