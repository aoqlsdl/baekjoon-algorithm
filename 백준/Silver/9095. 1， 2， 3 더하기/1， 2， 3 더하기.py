# 9095. 1, 2, 3 더하기
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    # dp table 초기화
    dp = [0] * 10000001

    for i in range(1, n + 1):
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            # 점화식
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])