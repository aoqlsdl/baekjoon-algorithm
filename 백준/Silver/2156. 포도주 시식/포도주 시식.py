import sys

input = sys.stdin.readline
n = int(input())
wi = [0]

for _ in range(n):
    w = int(input())
    wi.append(w)

dp = [0] * (n + 1)

dp[0] = 0


if n >= 1:
    dp[1] = wi[1]
if n >= 2:
    dp[2] = wi[1] + wi[2]
if n >= 3:
    for i in range(3, n + 1):
        # 현재 포도주 안 마시는 경우, 이전 잔을 안 마시고 현재 잔만 마시는 경우, 두 잔 연속 마시고 전전 잔은 안 마신 경우
        dp[i] = max(dp[i - 1], dp[i - 2] + wi[i], dp[i - 3] + wi[i - 1] + wi[i])

print(dp[n])