import sys

input = sys.stdin.readline
n, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= b[i - 1][0]: # 지금 물건을 담을 수 있는 경우
            dp[i][j] = max(b[i - 1][1] + dp[i - 1][j - b[i - 1][0]], dp[i - 1][j])
        else: # 현재 물건을 담을 수 없는 경우 
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])