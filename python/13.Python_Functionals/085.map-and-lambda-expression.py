# Problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# Programmer: Md. Ashraful Haque
# Date: 31.08.2024

cube = lambda x: x**3

def fibonacci(n):
    fibo_list = [0,1]
    for _ in range(2, n):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    
    return fibo_list[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))