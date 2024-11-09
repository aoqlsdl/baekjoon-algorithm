from bisect import bisect_left

t = int(input())

for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    b_arr.sort()

    for a in a_arr:
        cnt += bisect_left(b_arr, a)

    print(cnt)