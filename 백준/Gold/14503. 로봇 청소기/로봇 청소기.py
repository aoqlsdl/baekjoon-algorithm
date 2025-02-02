# 14503. 로봇 청소기
import sys

# 방의 크기
n, m = map(int, sys.stdin.readline().split())
# 로봇 청소기의 좌표
r, c, d = map(int, sys.stdin.readline().split())
# n*m 크기의 방
room = [list(map(int, input().split())) for _ in range(n)]

# 청소하는 room의 개수
res = 0

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

while True:
    # if not (0 <= r < n - 1 and 0 <= c < m - 1):
    #     continue

    # (r, c)가 청소되지 않았다면
    if room[r][c] == 0:

        room[r][c] = 2  # 청소 완료
        res += 1

    cnt = 0 # 방향 살펴본 횟수 초기화

    for i in range(4):
        d = (d + 3) % 4
        next_r = r + dx[d]
        next_c = c + dy[d]

        if (0 <= next_r < n - 1 and 0 <= next_c < m - 1) and room[next_r][next_c] == 0 :
            r = next_r
            c = next_c

            break

        cnt += 1

    if cnt == 4: # 다 살펴봤지만 아무곳에도 방문하지 못했다면
        next_r = r + dx[(d + 2) % 4]
        next_c = c + dy[(d + 2) % 4]

        if 0 <= next_r < n - 1 and 0 <= next_c < m - 1:
            if room[next_r][next_c] == 1:
                break

            r = next_r
            c = next_c
        else:
            break

print(res)