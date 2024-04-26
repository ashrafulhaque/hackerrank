# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Programmer: Md.Ashraful Haque
# Date: 21.04.2024

n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for _ in range(commands):
    cmd = input().split()
    
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))

print(sum(s))
