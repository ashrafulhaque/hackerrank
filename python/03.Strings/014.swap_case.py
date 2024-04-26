# Problem: https://www.hackerrank.com/challenges/swap-case
# Programmer: Md.Ashraful Haque
# Date: 05.04.2024

def swap_case(s):
    newstr = ""
    for c in s:
        if c.isnumeric():
            newstr += c
        elif c.islower():
            newstr += c.upper()
        else:
            newstr += c.lower()
    return newstr

def main():
    s = input()
    result = swap_case(s)
    print(result)


main()