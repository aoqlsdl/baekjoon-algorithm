import sys

input = sys.stdin.readline
n = int(input())
pa = [list(map(int, input().split())) for _ in range(n)]

b = 0 # 파란색 - 1
w = 0 # 흰색 - 0

def dfs(x, y, size): 
    global b, w

    std = pa[x][y]
    is_same = 1

    for i in range(size):
        for j in range(size):
            if pa[i + x][j + y] != std:
                is_same = 0
                break

    if is_same:
        if std == 1:
            b += 1
        else:
            w += 1
        return
    

    half = size // 2
    dfs(x, y, half)                # 좌상
    dfs(x, y + half, half)         # 우상
    dfs(x + half, y, half)         # 좌하
    dfs(x + half, y + half, half)  # 우하
        

dfs(0, 0, n)

print(w)
print(b)