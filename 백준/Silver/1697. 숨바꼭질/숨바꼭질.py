import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
res = 0 

v = [0] * 100001

q = deque()
q.append([n, 0])

while q:
    x, sec = q.popleft()

    if x < 0 or x > 100000:
        continue

    if x == k:
        res = sec
        break

    if v[x] == 0:
        q.append([x - 1, sec + 1])
        q.append([x + 1, sec + 1])
        q.append([x * 2, sec + 1])
        v[x] = 1

print(res)