# Problem: https://www.hackerrank.com/challenges/string-validators
# Programmer: Md. Ashraful Haque
# Date: 07.04.2024

s = input()

# Checks if str has any alphanumeric chars..
print(any(char.isalnum() for char in s))

# Checks if str has any alphabetical chars..
print(any(char.isalpha() for char in s))

# Checks if str has any digits..
print(any(char.isdigit() for char in s))

# Checks if str has any lowercase characters.
print(any(char.islower() for char in s))

# Checks if str has any uppercase characters.
print(any(char.isupper() for char in s))