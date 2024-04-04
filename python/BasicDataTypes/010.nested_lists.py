# Program: Nested Lists
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



"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and 
print the name(s) of any student(s) having the second lowest grade.

Input Format: 
The first line contains an integer,N, the number of students.
The subsequent lines describe each student over 2N lines.
- The first line contains a student's name.
- The second line contains their grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and 
print each one on a new line.
"""