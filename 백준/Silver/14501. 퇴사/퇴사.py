# 상담 적절히 했을 때 백준이가 얻을 수 있는 최대 수익

import sys

input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

# 1~N일차까지 순회하며 최대값을 확인하기
for i in range(n):
    for j in range(i + s[i][0], n + 1): # i번째 날에 상담을 진행했을 때 상담 가능한 모든 날짜
        if i + s[i][0] > n: # 상담 마지막날을 넘어갈 경우 패스
            continue
            
        if dp[j] < dp[i] + s[i][1]:
            dp[j] = dp[i] + s[i][1]

print(dp[n])