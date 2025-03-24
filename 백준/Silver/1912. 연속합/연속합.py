# 최대 연속합을 구하는 방법
# : 이전의 연속합과 현재 idx의 값을 더하는 경우 / 더하지 않는 경우 비교

# 점화식: max(dp[n - 1] + arr[n], arr[n])

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# dp 테이블 생성(이때, 음수가 있을 경우를 대비하여 n 크기의 리스트를 만든다.)
dp = [0] * n

# 0번째 idx에서의 최대합은 arr[0]
dp[0] = arr[0]

# 1 ~ n번째 idx일 때의 최대 합을 dp 테이블에 저장
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])

# dp 테이블에 저장된 값 중 가장 큰 값을 반환
print(max(dp))