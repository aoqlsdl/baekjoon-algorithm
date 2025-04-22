import sys
from collections import deque

dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]

w = 0 # 그림 넓이
mw = 0 # 그림의 최대 넓이
np = 0 # 그림의 개수

input = sys.stdin.readline
n, m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

v = [[0] * m for _ in range(n)]

# 너비 우선 처리 구현
q = deque()

for i in range(n):
    for j in range(m):
        if p[i][j] == 0 or v[i][j] != 0:
            continue

        q.append([i, j])
        v[i][j] = 1

        while q:
            x, y = q.popleft()
            w += 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                # 범위를 초과한다면 패스
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                # 이미 방문한 노드라면 패스
                if v[nx][ny] != 0:
                    continue

                # 그림 영역이 아니라면 패스
                if p[nx][ny] == 0:
                    continue

                q.append([nx, ny])
                v[nx][ny] = 1
        
        # q가 비어있다 == 하나의 그림을 모두 살펴보았다
        mw = max(mw, w)
        w = 0
        np += 1

print(np)
print(mw)