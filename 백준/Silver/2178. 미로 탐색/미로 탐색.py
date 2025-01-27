from collections import deque

# 2178. 미로탐색
n, m = map(int, input().split()) # 세로, 가로
maze = [[]]
visited = [[0] * (m + 1) for _ in range(n + 1)] # 방문 여부

for _ in range(n):
    elem = list(map(int, input()))
    elem.insert(0, 0)
    maze.append(elem)

dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]


# 최적 경로를 찾기 위해 BFS 사용
def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 미로 범위를 벗어나거나 0이거나 이미 방문한 경우 스킵
            if not (1 <= next_x <= n and 1 <= next_y <= m):
                continue
            if maze[next_x][next_y] == 0 or visited[next_x][next_y]:
                continue

            # 다음 칸으로 이동
            maze[next_x][next_y] += maze[x][y]
            visited[next_x][next_y] = 1  # 방문 처리
            queue.append([next_x, next_y])

bfs(1, 1)
print(maze[n][m])