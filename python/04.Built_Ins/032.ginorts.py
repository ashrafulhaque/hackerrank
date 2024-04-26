# Problem: https://www.hackerrank.com/challenges/ginorts/problem
# Programmer: Md.Ashraful Haque
# Date: 19.04.2024

s = sorted(input())
low = up = odd = even = ""
for i in s:
    if i.isalnum():
        if i.islower():
            low += i
        elif i.isupper():
            up += i
        else:
            if int(i) % 2 != 0:
                odd += i
            else:
                even += i

s = low + up + odd + even
print(s)


