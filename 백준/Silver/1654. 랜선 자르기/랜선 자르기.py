# 2805. 랜선 자르기
# 가장 긴 랜선을 기준으로 --> 여기서 s, e는 선의 시작과 끝이 아니라 선 길이의 범위로 잡아야 함
import sys

k, n = map(int, input().split())
ropes = [int(sys.stdin.readline()) for _ in range(k)]

s = 1 # 최소 선의 길이
e = max(ropes) # 가장 긴 선의 길이

result = 0

while s <= e:
    # 1. s, e 길이의 중간값을 구해서
    m = (s + e) // 2

    # 2. 그 중간값으로 모든 줄을 나눈 값에 따라서 좁힐 범위를 정하기
    devided_ropes = [r // m for r in ropes]
    n_ropes = sum(devided_ropes) # 잘린 랜선의 개수를 모두 더한 값

    # 3-1. 자른 랜선의 개수가 n개 이상일 경우, 현재 길이보다 더 길어질 수 있는지 확인해야 함
    if n_ropes >= n:
        s = m + 1
    # 3-2. 자른 랜선의 개수가 n개 미만일 경우, 현재 길이보다 더 짧은 범위에서 잘라봐야 함
    else:
        e = m - 1

print(e)
