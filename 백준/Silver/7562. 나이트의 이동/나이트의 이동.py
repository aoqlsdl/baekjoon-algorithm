import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

# 시계방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    # 테스트마다 큐 초기화 
    q = deque()

    s = int(input())
    n, m = map(int, input().split()) # 현재 위치
    ln, lm = map(int, input().split()) # 도착 위치
    ch = [[0] * s for _ in range(s)] # s x s 크기의 체스판
    v = [[0] * s for _ in range(s)] # 방문 여부 세팅

    q.append([n, m])

    # bfs 탐색
    while q:
        x, y = q.popleft()

        # 종료 조건
        if x == ln and y == lm:
            print(ch[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < s and 0 <= ny < s and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append([nx, ny])
                ch[nx][ny] = ch[x][y] + 1