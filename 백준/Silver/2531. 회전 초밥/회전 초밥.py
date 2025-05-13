import sys
from collections import defaultdict

input = sys.stdin.readline
n, d, k, c = map(int, input().split())

be = []

for _ in range(n):
    be.append(int(input()))

# 회전하는 것 고려하여 리스트 연장
be += be[:k - 1]

cnt = defaultdict(int)
num = 0 # 스시 종류
res = 0

# 처음 세팅
for i in range(k):
    if cnt[be[i]] == 0:
        num += 1

    cnt[be[i]] += 1

# 쿠폰 사용 여부 체크
res = num + (0 if cnt[c] else 1)

# 슬라이딩 윈도우
for i in range(1, n):
    # 왼쪽 제거
    cnt[be[i - 1]] -= 1

    if cnt[be[i - 1]] == 0:
        num -= 1

    # 오른쪽 추가
    if cnt[be[i + k - 1]] == 0:
        num += 1

    cnt[be[i + k - 1]] += 1
    
    
    res = max(res, num + (0 if cnt[c] else 1))

print(res)