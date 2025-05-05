import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

walls = []
virus = []

res = -sys.maxsize

# 벽, 바이러스 위치 저장
for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            virus.append((i, j))
        elif map[i][j] == 0:
            walls.append((i, j))

# 바이러스 퍼지는 과정 구현
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    
    # 벽이면 패스
    if map[x][y] == 1 or map[x][y] == 3:
        return
    
    map[x][y] = 3

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        dfs(nx, ny)
    
    
# 바이러스 위치 중 3개 조합을 뽑아 순회
for wa in combinations(walls, 3): 
    sz = 0
    for w in wa:
        map[w[0]][w[1]] = 1
    
    # 바이러스 퍼트리기
    for v in virus:
        vx = v[0]
        vy = v[1]
        dfs(vx, vy)
    
    # 바이러스 퍼진 후 안전지역 카운트, 최대값 갱신
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                sz += 1
                
            # 바이러스 감염된 곳이라면 원상 복구
            elif map[i][j] == 3:
                map[i][j] = 0
    
    

    res = max(sz, res)

    # 모든 연산 마무리 후 벽 세운 곳 원상 복구
    for w in wa:
        map[w[0]][w[1]] = 0

print(res)