# 1931. 회의실 배정
import sys

n = int(sys.stdin.readline().rstrip())
times = []

for _ in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    times.append(t)

# 끝나는 시간 오름차순 -> 시작 시간 오름차순 정렬
times.sort(key=lambda x: (x[1], x[0]))

# 회의 시작, 끝 초기화
start = times[0][0]
end = times[0][1]

# 회의 횟수 초기화
cnt = 1

for i in range(1, n):
    if times[i][0] >= end:
        start = times[i][0]
        end = times[i][1]
        cnt += 1


print(cnt)