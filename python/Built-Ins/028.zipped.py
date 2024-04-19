# Problem: https://www.hackerrank.com/challenges/zipped/problem
# Programmer: Md. Ashraful Haque
# Date: 19.04.2024

n, x = map(int,input().split())
marks = []
for i in range(x):
    marks.append([marks for marks in  map(float,input().split())])

zipped = zip(*marks)

for i in zipped:
    avg_mark = sum(i)/len(i)
    print(f"{avg_mark:.1f}")
