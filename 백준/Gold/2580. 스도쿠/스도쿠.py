import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
nxt = [(x, y) for x in range(9) for y in range(9) if board[x][y] == 0]

# 행, 열, 박스 별 숫자 사용 여부를 기록하는 배열
row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

# 기존 숫자들에 대해 기록
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num:
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i // 3) * 3 + (j // 3)][num] = True

def sudoku(n):
    if n == len(nxt):  # 모든 빈 칸을 채웠다면 출력 후 종료
        for row in board:
            print(*row)
        sys.exit(0)

    x, y = nxt[n]
    box_index = (x // 3) * 3 + (y // 3)

    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[box_index][num]:
            # 숫자 사용 기록
            board[x][y] = num
            row_used[x][num] = col_used[y][num] = box_used[box_index][num] = True

            sudoku(n + 1)

            # 백트래킹: 숫자 사용 취소
            board[x][y] = 0
            row_used[x][num] = col_used[y][num] = box_used[box_index][num] = False

sudoku(0)