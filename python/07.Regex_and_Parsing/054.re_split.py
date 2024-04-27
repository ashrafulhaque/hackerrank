# Problem: https://www.hackerrank.com/challenges/re-split/problem
# Programmer: Md.Ashraful Haque
# Date: 27.04.2024

regex_pattern = r"[\.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))