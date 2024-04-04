# Program: Touples
# Programmer: Md.Ashraful Haque
# Date: 04.04.2024

n = int(input())
integer_list = map(int, input().split())  # split input values based on space and map to integer object
data_tuple = tuple(integer_list) 
print(hash(data_tuple)) # use pypy3 to get a fixed value of hash


