import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]

# 치킨 거리 구하기 --> 도시의 치킨 거리의 최소값 구하기 가능
# 치킨집/집 위치 저장
chicken = []
house = []

min_d = sys.maxsize

for i in range(n):
    for j in range(n):
        if c[i][j] == 1:
            house.append((i, j)) # 집 좌표 저장
        elif c[i][j] == 2:
            chicken.append((i, j)) # 치킨집 좌표 저장

# 치킨집 m개를 뽑은 모든 경우의 수를 고려하기
for chick in combinations(chicken, m):
    d = 0 # 거리 초기화
    
    # 집을 하나씩 골라서, 각각의 치킨거리 도출
    for h in house:
        h_d = sys.maxsize # 한 가정 당 치킨거리 초기화
        for j in range(m):
            h_d = min(h_d, abs(h[0] - chick[j][0]) + abs(h[1] - chick[j][1]))
        d += h_d
    min_d = min(min_d, d)

print(min_d)
    