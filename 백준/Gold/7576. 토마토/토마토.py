import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

# 토마토 상자
ts = [list(map(int, input().split())) for _ in range(m)]

q = deque()

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# dfs 탐색
for i in range(m):
    for j in range(n):
        # 토마토가 익어있는 곳부터 시작
        if ts[i][j] == 1:
            q.append([i, j])

while q:
    x, y = q.popleft()
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < m and 0 <= ny < n:
            if ts[nx][ny] == 0: # 익지 않은 토마토에 전파
                ts[nx][ny] = ts[x][y] + 1
                q.append((nx, ny))

# 결과 계산
res = 0
for r in ts:
    for t in r:
        if t == 0:
            print(-1)
            exit()
        res = max(res, t)

print(res - 1)