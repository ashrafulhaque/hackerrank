# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Programmer: Md.Ashraful Haque
# Date: 22.04.2024

k = int(input())
room_numbers = list(map(int, input().split()))
s = set(room_numbers)
captains_room = (sum(s)*k -sum(room_numbers))//(k-1)
print(captains_room)