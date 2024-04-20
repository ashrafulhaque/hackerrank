# Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Programmer: Md.Ashraful Haque
# Date: 20.04.2024

def average(array):
    # set is used to find the distinct elements of the array
    array = set(array)
    avg = sum(array)/len(array)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)