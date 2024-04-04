# Program: Finding the percentage
# Programmer: Md. Ashraful Haque
# Date: 02.04.2024

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

query_scores = student_marks[query_name]
# print(query_score)
total = 0
for score in query_scores:
    total += score

avg = total/len(query_scores)
print("{0:.2f}".format(avg)) # prints 2 decimal places