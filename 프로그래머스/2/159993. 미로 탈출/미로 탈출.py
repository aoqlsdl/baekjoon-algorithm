from collections import deque

def bfs(start, end, maps):
	# 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    
    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    v = [[False]*m for _ in range(n)]
    q = deque()
    flag = False
    
    # 초깃값 설정
    for i in range(n):
        for j in range(m):
        	# 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
            if maps[i][j] == start:      
                q.append((i, j, 0))    
                # 별도의 cost 리스트를 만들지 않고 que에 바로 기록(0)
                v[i][j] = True
                flag = True; break 
                # 시작 지점은 한 개만 존재하기 때문에 찾으면 바로 나옴
        if flag: break
                
    # BFS 알고리즘 수행 (핵심)
    while q:
        y, x, cost = q.popleft()
        
        if maps[y][x] == end:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] !='X':
                if not v[ny][nx]:	# 아직 방문하지 않는 통로라면
                    q.append((ny, nx, cost+1))
                    v[ny][nx] = True
                    
    return -1	# 탈출할 수 없다면
        
            
def solution(maps):
    path1 = bfs('S', 'L', maps)	# 시작 지점 --> 레버
    path2 = bfs('L', 'E', maps) # 레버 --> 출구
    
    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
   	# 둘중 하나라도 -1 이면 탈출할 수 없음
    return -1