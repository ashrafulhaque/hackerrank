# Problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Programmer: Md.Ashraful Haque
# Date: 23.08.2024

from collections import OrderedDict

n = int(input())
ordered_data = OrderedDict()

for _ in range(n):
    item_name, price = input().rsplit(" ",1)
    price = int(price)
    if item_name not in ordered_data:
        ordered_data[item_name] = price
    else:
        ordered_data[item_name] += price

for i, j in ordered_data.items():
    print(i,j)
