# 1931 회의실 배정
import sys

n = int(sys.stdin.readline())
times = []

for _ in range(n):
    time = list(map(int, sys.stdin.readline().split()))
    times.append(time)

# 종료 시간을 기준으로 정렬
times.sort(key=lambda x: (x[1], x[0]))

# 종료 시간 초기화
end = times[0][1]

# 회의 횟수 초기화
cnt = 1

for i in range(1, n):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]

print(cnt)