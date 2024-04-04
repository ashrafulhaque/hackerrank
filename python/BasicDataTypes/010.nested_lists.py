# Problem: https://www.hackerrank.com/challenges/nested-list
# Programmer: Md.Ashraful Haque
# Date: 27.03.2024

students = []

# define number of students
n = int(input())

# use loop to input the names and grades of each student
for i in range(n):
    name = input()
    grade = float(input())

    # append one students[], note that, append() takes one arg. only
    students.append([name,grade])
#end data inputs/for loop

# Sort the 2D list based on the 2nd element in each sublist using LAMBDA function
students = sorted(students,key=lambda x:x[1])

# create a list to store the name(s) of 2nd lowest graders
second_lowest = [] 
lowest_score = students[0][1]
temp = 0
# Skip the first element/lowest grade to get 2nd lowest
for name,grade in students[1:]:
    if temp == 0 or temp == grade:
        # since there could be multiple lowest values,we need to skip them
        if grade != lowest_score:
            second_lowest.append(name)
            temp = grade

# sort the output list alphabetically
second_lowest.sort()
for name in second_lowest:
    print(name)
