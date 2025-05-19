import sys


def dfs(st):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    # n개를 기준으로 순회
    for i in range(st, n + 1):
        if i in arr:
            continue

        arr.append(i)

        dfs(i + 1)

        # dfs문에서 탈출한 후에는 반드시 초기화
        arr.pop()


input = sys.stdin.readline
n, m = map(int, input().split())
arr = []

dfs(1)