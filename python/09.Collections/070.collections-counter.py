# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Programmer: Md.Ashraful Haque
# Date: 21.08.2024

from collections import Counter

num_of_shoes = int(input().strip())
shoe_sizes = list(map(int, input().split(" ")))
num_of_customers = int(input().strip())

# Dictionary contining shoe sizes and amounts of each sizes
sizes_and_amounts = Counter(shoe_sizes)
# dict.keys() returns dictionary view of all the keys in the dict
sizes = list(Counter(shoe_sizes).keys())
# dict.values() returns dictionary view of all the values in the dict
amount_for_each_size = list(Counter(shoe_sizes).values())

total_earning = 0

for _ in range(num_of_customers):
    desired_size, price = map(int, input().split(" "))
    
    if desired_size in sizes:
        index = sizes.index(desired_size)
        if amount_for_each_size[index] > 0:
            total_earning += price
            amount_for_each_size[index] -= 1

print(total_earning)


