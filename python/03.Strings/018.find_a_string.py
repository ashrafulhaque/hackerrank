# Problem: https://www.hackerrank.com/challenges/find-a-string/
# Programmer: Md.Ashraful Haque
# Date: 05.04.2024

def count_substring(string, sub_string):
    count = 0
    n = len(string) - len(sub_string) + 1
    
    for i in range(n):
        if string[i:len(sub_string)+i] == sub_string:
            count += 1 
    return count

def main():
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

main()