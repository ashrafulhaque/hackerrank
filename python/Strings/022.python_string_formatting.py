# Problem: https://www.hackerrank.com/challenges/python-string-formatting
# Programmer: Md. Ashraful Haque
# Date: 08.04.2024

def print_formatted(number):
    space = len(format(number, 'b'))
    for i in range(1, number+1):
       print (f"{str(i).rjust(space)} {format(i, 'o').rjust(space)} {format(i, 'X').rjust(space)} {format(i, 'b').rjust(space)}")

def main():
    n = int(input())
    print_formatted(n)

main()