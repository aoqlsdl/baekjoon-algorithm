import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())


def recursive(size):
    # *을 넣는 칸의 사이즈가 1일 때(가장 작은 범위일 때) 별 찍고 탈출
    if size == 1:
        return ['*']

    star = recursive(size // 3)

    res = []

    for s in star:
        res.append(s * 3)

    for s in star:
        res.append(s + " " * (size // 3) + s)

    for s in star:
        res.append(s * 3)

    return res


recursive(n)
print('\n'.join(recursive(n)))