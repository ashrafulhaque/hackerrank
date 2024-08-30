# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem
# Programmer: Md.Ashraful Haque
# Date: 30.08.2024

import os
from datetime import datetime

def time_delta(t1, t2):
    # Define the format of the input timestamps
    time_format = "%a %d %b %Y %H:%M:%S %z"
    
    # Parse the timestamps into datetime objects
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    
    # Calculate the difference between the two datetime objects
    delta = abs((dt1 - dt2).total_seconds())
    
    # Return the difference as a string
    return str(int(delta))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()