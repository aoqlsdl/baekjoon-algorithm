import sys

n, r, c = map(int, sys.stdin.readline().split())


# r행 c열이 0,0이 될 때까지 확인
def recursive(r, c, n):
    if n == 0:
        return 0

    half = 2 ** (n - 1)

    if r < half and c < half:  # 좌상단
        return recursive(r, c, n - 1)
    elif r < half and c >= half:  # 우상단
        return recursive(r, c - half, n - 1) + half * half
    elif r >= half and c < half:  # 좌하단
        return recursive(r - half, c, n - 1) + 2 * half * half
    else:  # 우하단
        return recursive(r - half, c - half, n - 1) + 3 * half * half

print(recursive(r, c, n))