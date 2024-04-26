# Problem: https://www.hackerrank.com/challenges/python-mutations
# Programmer: Md.Ashraful Haque
# Date: 05.04.2024

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)