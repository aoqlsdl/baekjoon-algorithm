import sys

n, m = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

# 잘린 목재 --> 나무 - 절단기 길이 뺀 값을 구해야 함
s = 1 # 절단기의 최소 길이
e = max(trees) # 가장 긴 나무의 길이를 절단기의 최대 길이로 설정

while s <= e:
    # 잘린 목재 길이 초기화
    tree_len = 0

    mid = (s + e) // 2

    divided_trees = [t - mid for t in trees if t > mid]
    tree_len = sum(divided_trees)

    if tree_len >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)

