# 14891. 톱니바퀴
import collections
import sys

# 하나 움직이면 주변에 있는 다른 것도 똑같이 움직이고, 그 다른 게 움직이면 그 옆에 있는 다른 것들도 똑같이 움직여야 하고... --> 재귀?

wheels = []

for _ in range(4):
    # 회전시키기 위해 deque로 담기
    wheels.append(collections.deque(list(input())))

k = int(sys.stdin.readline())


def left_wheel(n, m):
    if n < 0: # 첫 번째 톱보다 앞에 있으면 확인 x
        return
    if wheels[n][2] != wheels[n + 1][6]: # 극이 다를 때만 회전
        left_wheel(n - 1, -m) # 왼쪽에 있는 바퀴도 확인하고 회전시킨 다음
        wheels[n].rotate(m) # 이 바퀴를 회전시켜야 함

def right_wheel(n, m):
    if n > 3: # 마지막 톱을 지나쳤으면 확인 x
        return
    if wheels[n - 1][2] != wheels[n][6]:
        right_wheel(n + 1, -m)
        wheels[n].rotate(m)


for _ in range(k):
    n, m = map(int, sys.stdin.readline().split())
    n -= 1 # 인덱스를 앞으로 한 칸씩 조정
    left_wheel(n - 1, -m) # 방향은 항상 반대로 움직임
    right_wheel(n + 1, -m) # 방향은 항상 반대로 움직임
    wheels[n].rotate(m)

result = 0

if wheels[0][0] == '1':
    result += 1
if wheels[1][0] == '1':
    result += 2
if wheels[2][0] == '1':
    result += 4
if wheels[3][0] == '1':
    result += 8

print(result)