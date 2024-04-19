# Problem: https://www.hackerrank.com/challenges/capitalize
# Programmer: Md. Ashraful Haque
# Date: 18.04.2024

def solve(s):
    name = list(s.split(" "))
    final_name = ""
    for i in name:
            if len(final_name) == 0:
                final_name +=  i.capitalize()
            else:
                 final_name += " " + i.capitalize()
    return final_name
         
def main():
    fptr = open("capitalize.txt", 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

main()