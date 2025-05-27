import sys

def dfs(x, y, size):

    std = vid[x][y]
    is_same = 1

    # 영상 내의 숫자가 모두 동일한지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if vid[i][j] != std:
                is_same = 0
                break
        if not is_same:
            break
    
    # 모두 동일하다면 기준이 되는 수를 return
    if is_same:
        return str(std)
    
    half = size // 2
    
    # 상좌 / 상우 / 하좌 / 하우 순으로 탐색
    tl = dfs(x, y, half)
    tr = dfs(x, y + half, half)
    bl = dfs(x + half, y, half)
    br = dfs(x + half, y + half, half)

    return f"({tl}{tr}{bl}{br})"


n = int(sys.stdin.readline())
vid = [[int(i) for i in sys.stdin.readline().strip()] for _ in range(n)]

res = dfs(0,0,n)
print(res)