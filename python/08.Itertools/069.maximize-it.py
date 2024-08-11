# Problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Programmer: Md.Ashraful Haque
# Date: 11.08.2024

from itertools import product

# get the inputs
numOfLists, moduloValue = map(int, input().split(' '))
chainOfLists = []

for i in range(numOfLists):
    newList = list(map(int, input().split(' '))) # map values to int split by spaces and convert to list
    chainOfLists.append(newList[1:]) # append every new list to the listOfLists from index 1 to end

# find cartesian product (all combinations) of the lists taking 1 element from each list 
oneValueFromEachList = list(product(*chainOfLists)) # don't forget the * to get values

# list of Sum of Squares 
sosList = [] 

# loop through the combinations  
for comboList in oneValueFromEachList:
    sumOfSquare = 0
    for value in comboList:
        sumOfSquare = sumOfSquare + (value**2)
    # end inner for loop

    result = sumOfSquare % moduloValue
    sosList.append(result)   
# end outer for loop

print(max(sosList))
