# 2012. 등수 매기기
import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)

arr.sort()
cnt = 0

for i in range(1, n + 1):
    if i > arr[i - 1]:
        cnt += -1 * (arr[i - 1] - i)
    elif i + 1 <= arr[i - 1]:
        cnt += arr[i - 1] - i


print(cnt)