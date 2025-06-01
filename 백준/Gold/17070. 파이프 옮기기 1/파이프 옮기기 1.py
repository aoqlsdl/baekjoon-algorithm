import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
hou = [list(map(int, input().split())) for _ in range(n)]

# dp[x][y][d]: (x, y)에 파이프 끝이 있고 방향 d일 때 가능한 경우의 수
dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]

# 이동 가능 여부 확인
def canMove(x, y):
    return 0 <= x < n and 0 <= y < n and hou[x][y] == 0

def dfs(x, y, d):
    # 끝에 도달하면 경우의 수 1
    if x == n - 1 and y == n - 1:
        return 1

    if dp[x][y][d] != -1:
        return dp[x][y][d]

    dp[x][y][d] = 0

    if d == 0:  # 가로
        if canMove(x, y + 1):
            dp[x][y][d] += dfs(x, y + 1, 0)
        if canMove(x + 1, y) and canMove(x, y + 1) and canMove(x + 1, y + 1):
            dp[x][y][d] += dfs(x + 1, y + 1, 2)

    elif d == 1:  # 세로
        if canMove(x + 1, y):
            dp[x][y][d] += dfs(x + 1, y, 1)
        if canMove(x + 1, y) and canMove(x, y + 1) and canMove(x + 1, y + 1):
            dp[x][y][d] += dfs(x + 1, y + 1, 2)

    elif d == 2:  # 대각선
        if canMove(x, y + 1):
            dp[x][y][d] += dfs(x, y + 1, 0)
        if canMove(x + 1, y):
            dp[x][y][d] += dfs(x + 1, y, 1)
        if canMove(x + 1, y) and canMove(x, y + 1) and canMove(x + 1, y + 1):
            dp[x][y][d] += dfs(x + 1, y + 1, 2)

    return dp[x][y][d]

# 시작은 (0, 1)에 가로 방향
if hou[n - 1][n - 1] == 1:
    print(0)
else:
    print(dfs(0, 1, 0))