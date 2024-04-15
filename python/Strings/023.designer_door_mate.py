# Problem: https://www.hackerrank.com/challenges/designer-door-mat/
# Programmer: Md. Ashraful Haque
# Date: 15.04.2024

n, m = [int(x) for x in input().split()]  

half = n // 2
dash = (m - 3) // 2
periods_and_pipe = 1 

# prints the upper half design of the mat
for i in range(half):
    print("-" * dash + ".|." * periods_and_pipe + "-" * dash)
    dash -= 3
    periods_and_pipe += 2
    
# prints the middle line of the mat
mid_line_dash = (m - 7) // 2 
print("-" * mid_line_dash + "WELCOME" + "-" * mid_line_dash)

# prints the lower half design of the mat
for i in range(half):
    dash += 3
    periods_and_pipe -= 2
    print("-" * dash + ".|." * periods_and_pipe + "-" * dash)
    