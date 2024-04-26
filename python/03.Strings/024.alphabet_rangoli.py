# problem: https://www.hackerrank.com/challenges/alphabet-rangoli
# programmer: Md. Ashraful Haque
# date: 15.04.2024

def print_rangoli(size):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # actual list based on size
    temp_list = alphabets[0:size]
    rows = (size*2) -1
    half_dash = (size-1) * 2
    num_of_ch = 1

    for i in range(rows+1):
        if i == size:
            half_dash += 4
            num_of_ch -= 2
            continue
        # prints first dashes in a line
        print("-" * half_dash, end='')
        k = size - 1
        for j in range(num_of_ch):
            print(temp_list[k], end='')
            if num_of_ch != 1:
                print("-", end='')
            k -= 1
        k = k+2
        for j in range(num_of_ch-1):
            print(temp_list[k], end='')
            if j < num_of_ch-2:
                print("-", end='')
            k = k + 1
        # prints last dashes in a line
        print("-" * half_dash)
        if i < size:
            num_of_ch += 1
            half_dash -= 2
        else:
            half_dash += 2
            num_of_ch -= 1

def main():
    n = int(input())
    print_rangoli(n)

main()  