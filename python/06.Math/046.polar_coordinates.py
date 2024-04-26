# Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Programmer: Md.Ashraful Haque
# Date: 26.04.2024

from cmath import phase

z = complex(input().strip())
modolus_r = abs(z)
phase_angle = phase(z)

print(f"{modolus_r}\n{phase_angle}")