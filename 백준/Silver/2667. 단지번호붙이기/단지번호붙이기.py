# 3/2 숙제

# 함수 정의

def dfs(x, y):
    # 범위를 벗어났다면 false
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 이미 방문했다면
    if v[x][y] == 1:
        return False

    # 집이 있다면 가구수 추가
    if m[x][y] == 1:
        global h
        h += 1
        
        # 방문 처리
        v[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        
        # dfs 탐색 후 true 반환
        return True
    
    # 집이 없다면 false 반환
    return False

# 문제 풀이
import sys

# 입력값
n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 여부 기록
v = [[0] * n for _ in range(n)]

# 가구 수 저장
homes = []

# 각 가구 수
h = 0

# 단지 수
c = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            homes.append(h)
            
            # 단지수 추가
            c += 1

            # 가구수 초기화
            h = 0

homes.sort()

print(c)
for i in range(len(homes)):
    print(homes[i])