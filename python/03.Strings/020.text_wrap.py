# Problem: https://www.hackerrank.com/challenges/text-wrap
# Programmer: Md. Ashraful Haque
# Date: 07.04.2024

import textwrap

def wrap(string, max_width):
    text = textwrap.wrap(string, max_width)
    result = ""
    for i in text:
        result +=  i + "\n"
    return result

def main():
    string = input()
    max_width = int(input())
    
    result = wrap(string, max_width)
    print(result)

main()