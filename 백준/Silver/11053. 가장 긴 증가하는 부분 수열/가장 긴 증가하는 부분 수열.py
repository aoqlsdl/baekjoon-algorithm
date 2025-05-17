import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# dp 테이블 설정
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))