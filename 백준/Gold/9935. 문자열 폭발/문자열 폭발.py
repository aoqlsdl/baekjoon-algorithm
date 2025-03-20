import os

arr = list(input())
bomb = input()
len_bomb = len(bomb)

result = []

for a in arr:
    result.append(a)

    if len(result) < len_bomb:
        continue

    if ''.join(result[-len_bomb:]) == bomb:
        del result[-len_bomb:]

if len(result) == 0:
    print("FRULA")
else:
    print(''.join(result))