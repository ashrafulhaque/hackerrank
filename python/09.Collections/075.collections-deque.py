# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Programmer: Md.Ashraful Haque
# Date: 23.08.2024

from collections import deque

dq_container = deque()

for _ in range(int(input())):
    command = input()
    if command == 'pop':
        dq_container.pop()
    elif command == 'popleft':
        dq_container.popleft()
    else:
        cmd, value = map(str, command.split(" "))
        value = int(value)
        
        if cmd == 'append':
            dq_container.append(value)
        elif cmd == 'appendleft':
            dq_container.appendleft(value)

for item in dq_container:
    print(item, end=" ")

print()
