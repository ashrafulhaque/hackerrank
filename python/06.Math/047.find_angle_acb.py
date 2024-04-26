# Problem: https://www.hackerrank.com/challenges/find-angle/problem
# Programmer: Md.Ashraful Haque
# Date: 26.04.2024

import math

ab = float(input().strip())
bc = float(input().strip())

hypo = math.sqrt(ab**2 + bc**2)
angle_radian = math.asin(ab/hypo)
angle_degree = round(math.degrees(angle_radian))

print(f"{angle_degree}\N{DEGREE SIGN}")



