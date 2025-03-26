import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

# dp[i] = dp[j]의 최댓값 + arr[i] (이때, 0 <= j < i)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
        else:
            dp[i] = max(dp[i], arr[i])

print(max(dp))