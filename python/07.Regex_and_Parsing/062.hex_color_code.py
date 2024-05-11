# Program: https://www.hackerrank.com/challenges/hex-color-code/problem
# Programmer: Md.Ashraful Haque
# Date: 11.05.2024

import re
n = int(input().strip())
results = []

for _ in range(n):
    css = input().strip()
  #(?<!^): This negative lookbehind assertion ensures that the '#' character is not at the beginning of the line
    color_codes = re.findall(r"(?<!^)(#[0-9A-Fa-f]{3,6})", css)
    if (color_codes):
        results.append(color_codes)

flattened_colors = [color for sublist in results for color in sublist]
for i in flattened_colors:
    print(i)