import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
std = list(map(int, input().split()))

pic = [] # 사진틀

# 이미 추천받은 학생인지 확인하는 함수
def isExists(s):
    for j in range(len(pic)):
        if s == pic[j][0]:
            return j
        
    return -1

for i in range(m):
    s = std[i]
    idx = isExists(s)

    # 이미 사진틀에 있는 학생이면 추천 수만 증가
    if idx != -1:
        pic[idx][1] += 1
        continue

    # 학생을 사진틀에 추가
    if len(pic) < n:
        pic.append([s, 1, i]) # 학생 번호 / 추천 횟수 / 추천 시점
        
    # 학생 수가 꽉 찼을 경우
    else:
        pic.sort(key=lambda x : (x[1], x[2])) # 추천수가 가장 적으면서 추천을 받은지 오래된 학생 제거
        pic.pop(0)
        # 새로운 학생 추가
        pic.append([s, 1, i])
        continue
        

pic.sort(key=lambda x:x[0])

for p in pic:
    print(p[0], end=" ")
