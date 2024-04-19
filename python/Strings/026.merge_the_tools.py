# Problem: https://www.hackerrank.com/challenges/merge-the-tools/
# Programmer: Md. Ashraful Haque
# Date: 19.04.2024

def merge_the_tools(string, k):
    substr_list = [string[i:i+k] for i in range(0, len(string), k)]
    
    for substr in substr_list:
        rem_occur = ""
        for c in substr:
            if c not in rem_occur:
                rem_occur += c

        print(rem_occur)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)