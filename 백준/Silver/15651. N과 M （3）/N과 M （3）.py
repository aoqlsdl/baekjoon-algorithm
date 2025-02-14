import sys

n, m = map(int, sys.stdin.readline().split())
a = [0 for _ in range(m)] # m개 만큼 고를 수 있는 수를 저장

def recursive(cnt):
    if cnt == m: # m번째 자리까지 조회했다면 print
        print(' '.join(map(str, a)))
        return
    for i in range(1, n + 1): # 1부터 n까지 자연수 중에서
        a[cnt] = i # a[0] = 1이면 [1, x, y, ...]
        recursive(cnt + 1) # a[1] -> 즉 두 번째 숫자에 대해서 오름차순으로 조회

recursive(0)