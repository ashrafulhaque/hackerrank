# Problem: https://www.hackerrank.com/challenges/most-commons/problem
# Programmer: Md.Ashraful Haque
# Date: 26.08.2024

from collections import Counter

if __name__ == '__main__':
    s = input()
    # Step 1: Create a Counter object directly from the string
    counter = Counter(s)

    # Step 2: Sort all characters by frequency and then alphabetically
    sorted_characters = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

    # Step 3: Get the top 3 characters
    top_three = sorted_characters[:3]

    # Step 4: Print the results
    for i, j in top_three:
        print(i, j)