# 3/2 숙제
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -sys.maxsize
min_val = sys.maxsize

def recur(idx, res, add, sub, mul, div):
    global max_val, min_val

    # 모든 숫자를 사용한 경우 최대, 최솟값 갱신
    if idx == n:
        max_val = max(max_val, res)
        min_val = min(min_val, res)
        return
    
    # 덧셈 연산
    if add > 0:
        recur(idx + 1, res + nums[idx], add - 1, sub, mul, div)
    
    # 뺄셈 연산
    if sub > 0:
        recur(idx + 1, res - nums[idx], add, sub - 1, mul, div)

    # 곱셈 연산
    if mul > 0:
        recur(idx + 1, res * nums[idx], add, sub, mul - 1, div)

    # 나눗셈 연산
    if div > 0:
        # 양수일 때는 그대로 나누고
        if res > 0:
            recur(idx + 1, res // nums[idx], add, sub, mul, div - 1)
        # 음수일 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾸기
        else:
            recur(idx + 1, -(-res // nums[idx]), add, sub, mul, div - 1)

recur(1, nums[0], add, sub, mul, div)
print(max_val)
print(min_val)