import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    # arr에서 i개를 뽑은 모든 조합을 살펴보기
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)