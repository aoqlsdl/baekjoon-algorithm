T = int(input())
for test_case in range(1, T + 1):
    a, b, n = map(int, input().split())
    cnt = 0

    while a <= n and b <= n:
        if a > b:
            b += a
        else:
            a += b
        cnt += 1

    print(cnt)
