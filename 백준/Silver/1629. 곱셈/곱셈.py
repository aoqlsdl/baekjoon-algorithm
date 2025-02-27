import sys

sys.setrecursionlimit(10**6)

a, b, c = map(int, sys.stdin.readline().split())


# 10^11 = 10^5 * 10^5 * 10
# 10^5 = 10^2 * 10^2 * 10
# 10^2 = 10^1 * 10^1
# 10^1 ==> 더이상 나눌 수 없음
def recursive(a, b, c):
    # 지수가 1이라면 탈출
    if b == 1:
        return a % c

    # a를 절반으로 나누어주기
    k = recursive(a, b // 2, c)

    if b % 2 == 0:
        return (k * k) % c
    else:
        return (k * k * a) % c


print(recursive(a, b, c))