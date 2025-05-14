import sys

input = sys.stdin.readline

n, k = map(int, input().split())
S = list(map(int, input().split()))

# 최장길이
res = 0

# 시작/끝 idx
st = 0
en = 0

# 홀/짝 카운팅
cnt = 0

# en의 위치가 리스트를 벗어나기 전까지 슬라이딩 윈도우 연산 실행
while en < n:
    # en 이동 시키기
    en += 1

    # en 홀짝 확인
    if S[en - 1] % 2 != 0:
        cnt += 1
    
    # 홀수가 k개보다 많다면, 홀수의 개수가 k 이하가 될 때까지 시작 지점 모두 이동
    while cnt > k and en < n:
        # 시작 idx는 개수 카운팅에서 빼주고,
        if S[st] % 2 != 0:
            cnt -= 1
        
        st += 1
        
    # 최대 길이 갱신
    res = max(res, en - st - cnt) # 리스트의 길이 - 홀수의 개수

print(res)