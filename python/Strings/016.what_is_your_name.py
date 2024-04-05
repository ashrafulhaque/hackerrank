# Problem: https://www.hackerrank.com/challenges/whats-your-name/problem
# Programmer: Md.Ashraful Haque
# Date: 05.04.2024

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

def main():
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

main()