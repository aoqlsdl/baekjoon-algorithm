import sys
import math

n = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(math.log(n, 3)) # n이 3의 몇 제곱인지 구하기

num1 = 0 # 1의 개수
num2 = 0 # 0의 개수
num3 = 0 # -1의 개수

def recursive(x, y, size):
    global num1, num2, num3

    # 모든 종이가 같은 종류인지 확인
    arr = set()
    for a in range(x, x + size):
        for b in range(y, y + size):
            arr.add(p[a][b])

     # 같은 종류라면 수의 종류에 따라 카운팅하고 탈출
    if len(arr) == 1:
        if -1 in arr:
            num1 += 1
        elif 0 in arr:
            num2 += 1
        elif 1 in arr:
            num3 += 1

        return

    # 서로 다른 수가 2개 이상이라면 더 작은 범위로 살펴보기
    n_size = size // 3 # 살펴보는 크기를 더 쪼개기
    for dx in range(3):
        for dy in range(3):
            recursive(x + dx * n_size, y + dy * n_size, n_size)
    
        


recursive(0,0,n)

print(num1)
print(num2)
print(num3)