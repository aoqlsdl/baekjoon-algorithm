# 20055. 컨베이어 벨트 위의 로봇
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
convey = deque(map(int, input().split()))
bots = [] # 여기도 deque을 사용해서 pop
steps = 0

while True:
    steps += 1
    # 2. 컨베이어를 한 칸 회전
    convey.rotate(1)
    bots = [ # 리스트 내 모든 요소에 대해서 idx 위치를 한 칸씩 업데이트
        (bot + 1) % (2 * n) for bot in bots
    ]

    # 리스트 내에 n(내리는 위치)이 포함되어 있다면 제거
    if n - 1 in bots:
        bots.remove(n - 1)

    # 3. 로봇을 한 칸 이동
    # 3-1. 다음 idx의 값 확인 (로봇이 있는 칸의 위치를 어떻게 알 수 있을지. => 따로 list 생성)
    for i in range(len(bots)):
        # 다음 idx의 내구도가 0이거나, 현재 인덱스 값 + 1 값이 이미 리스트에 존재한다면 패스
        if convey[(bots[i] + 1) % (2 * n)] <= 0 or (bots[i] + 1) % (2 * n) in bots :
            continue

        # 다음 idx의 내구도가 1 이상이면,
        # 3-1-1. 로봇의 idx를 한 칸 이동
        bots[i] = (bots[i] + 1) % (2 * n)
        # 3-1-2. 이동한 칸의 내구도 -= 1
        convey[bots[i]] -= 1

    # 리스트 내에 n(내리는 위치)이 포함되어 있다면 제거
    if n - 1 in bots:
        bots.remove(n - 1)


    # 1. 컨베이어에 로봇 올리기
    if convey[0] > 0 and 0 not in bots:
        convey[0] -= 1
        bots.append(0)

    # 3-2. 내구도 0인 칸의 개수 확인
    cnt = convey.count(0)

    if cnt >= k:
        break


print(steps)