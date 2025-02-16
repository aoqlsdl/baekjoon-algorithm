def row(a, n):
    for i in range(9):
        if a == s[n][i]:
            return False
    return True


def col(a, n):
    for i in range(9):
        if a == s[i][n]:
            return False
    return True


def square(x,y,a):
    for i in range(3):
        for j in range(3):
            if a == s[y//3*3+i][x//3*3+j]:
                return False
    return True

def recursive(n):
    if n == len(z):

        for i in s:
            print(*i)
        exit()

    for i in range(1,10):
        y = z[n][0]
        x = z[n][1]

        if row(i, y) and col(i, x) and square(x,y,i):
            s[y][x] = i
            recursive(n + 1)
            s[y][x] = 0


import sys

s = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
z = []
for i in range(9):
    for j in range(9):
        if s[i][j] == 0:
            z.append([i,j])
recursive(0)