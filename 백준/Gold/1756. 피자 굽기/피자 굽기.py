import sys

d, n = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
pizza = list(map(int, sys.stdin.readline().split()))

# 현재 idx의 너비가 이전 idx의 너비보다 크다면 현재 idx의 너비를 이전 idx의 너비로 설정
for i in range(1, d):
    oven[i] = min(oven[i], oven[i - 1])

# 가장 깊은 곳에서부터 올라오면서 피자를 넣을 수 있는 위치 확인
pos = d

for p in pizza:
    # 오븐을 탐색중이면서 오븐의 너비가 p보다 좁을 때 위치를 계속 위로 올리기
    while pos > 0 and oven[pos - 1] < p:
        pos -= 1
    
    # 오븐 밖으로 빠져나왔다면
    if pos == 0:
        break
    
    # 피자를 해당 위치에 올리기
    pos -= 1

if pos == 0:
    print(pos)
else:
    print(pos + 1)