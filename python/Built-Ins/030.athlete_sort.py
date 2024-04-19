# Problem: https://www.hackerrank.com/challenges/python-sort-sort/problem
# Programmer: Md.Ashraful Haque
# Date: 19.04.2024

def key_sort(li_of_li,key):
    li_of_li.sort(key=lambda x:x[key])
    return li_of_li


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    li_of_li = key_sort(arr,k)
    
    for li in li_of_li:
        for i in li:
            print(i,end=" ")
        print()