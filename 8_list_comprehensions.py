# Program: List Compregensions
# Programmer: Md. Ashraful Haque
# Date: 26.03.2024

x = int(input())
y = int(input())
z = int(input())
n = int(input())

permutaions = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k) != n]
print(permutaions)



"""
You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (x,y,z) on a 3D grid where the sum of i+j+k is not equal to n.
Sample Input: 1 1 1 2
Sample Output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""