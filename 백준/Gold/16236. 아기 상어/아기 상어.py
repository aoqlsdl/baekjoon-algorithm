import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
sp = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]

x, y = 0, 0 # 아기상어 위치
ss = 2 # 아기상어 크기
nf = 0 # 먹은 물고기 수
t = 0 # 먹는데 걸리는 시간 

dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]

q = deque()
hq = []

for i in range(n):
    for j in range(n):
        if sp[i][j] == 9:
            x, y = i, j

while True:
    q.append((x, y))
    # 거리 초기화
    d[x][y] = 0
    
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 이동 범위 내에서 최소 거리 측정
            if 0 <= nx < n and 0 <= ny < n:
                # 방문 여부 체크
                if d[nx][ny] == 0 and (sp[nx][ny] == 0 or sp[nx][ny] == ss):
                    d[nx][ny] = d[cx][cy] + 1
                    q.append((nx, ny))

                elif d[nx][ny] == 0 and 0 < sp[nx][ny] < ss:
                    d[nx][ny] = d[cx][cy] + 1
                    heapq.heappush(hq, (d[nx][ny], nx, ny))

    if len(hq) == 0:
        print(t)
        break
        
    # 최소 거리 갱신
    else:
        ti, nx, ny = heapq.heappop(hq)
        t += ti

        # 상어가 이동하므로, 기존 자리를 0으로 만들고 새 위치에서 먹은 물고기 지우기
        sp[x][y] = 0
        
        x, y = nx, ny
        sp[x][y] = 0
    
        nf += 1
        if nf == ss:
            nf = 0
            ss += 1
        
        # 리스트 초기화
        hq = []
        d = [[0] * n for _ in range(n)]
    
