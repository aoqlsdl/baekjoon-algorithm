import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]

bs = []
visited = [[0] * m for _ in range(n)]

res = -sys.maxsize

# 아기상어, 빈 공간 위치 저장
for i in range(n):
    for j in range(m):
        if sea[i][j] == 1:
            bs.append((i, j))

# bfs를 이용한 최단거리 측정 
dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 북/북동/동/동남/남/남서/서/서북
dy = [0, 1, 1, 1, 0, -1, -1, -1]

q = deque()

for b in bs:
    q.append([b[0], b[1]])
    visited[b[0]][b[1]] = 1

while q:
    x, y = q.popleft()

    # 대각선을 포함해 순회
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        # 거리는 -1 해줘야 함
        res = max(visited[i][j] - 1, res)

print(res)