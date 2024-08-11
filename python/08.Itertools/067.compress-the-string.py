# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# Programmer: Md.Ashraful Haque
# Date: 11.08.2024

from itertools import groupby

textInput = input().strip()

# group the textInput by the default key (none) 
groupedText = groupby(textInput)

for key, value in groupedText:
    key = int(key) # make the key integer value for output
    value = len(list(value)) # get the lenth of the list of rereated value from object for output
    touple = (value, key) # make a touple by value,key as epected output 
    print(touple, end=' ') # print the key and how many repetition

print() # for ending \n