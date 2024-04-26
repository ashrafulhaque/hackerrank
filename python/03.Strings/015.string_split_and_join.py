# Problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# Programmer: Md.Ashraful Haque
# Date: 05.04.2024

def split_and_join(line):
    list_of_words = line.split()
    list_of_words = ("-").join(list_of_words)
    return list_of_words

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)