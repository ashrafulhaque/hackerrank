# Problem: https://www.hackerrank.com/challenges/python-lists
# Programmer: Md.Ashraful Haque
# Date: 04.04.2024


data_list = [] # list to keep all the numbers 

N = int(input())

for _ in range(N):
    option = input().split()
    operation = option[0]

    if len(option) == 3:
        if operation == "insert":
            data_list.insert(int(option[1]),int(option[2]))
    elif len(option) == 2:
        if operation == "append":
            data_list.append(int(option[1]))
        elif operation == "remove":
            data_list.remove(int(option[1]))
    elif len(option) == 1:
        if operation == "print":
            print(data_list)
        elif operation == "pop":
            data_list.pop()
        elif operation == "sort":
            data_list.sort()
        elif operation == "reverse":
            data_list.reverse()
        