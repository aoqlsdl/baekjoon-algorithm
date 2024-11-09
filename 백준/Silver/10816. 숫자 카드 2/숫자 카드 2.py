from bisect import bisect_left, bisect_right

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
sample = list(map(int, input().split()))

# 상근이의 카드를 이분탐색하기 위해 오름차순으로 정렬
cards.sort()

# sample 리스트를 순회하며 카드의 수 확인
start = 0
end = n - 1

def card_count(arr, start, end, s):
    mid = int((start + end) // 2)

    if arr[mid] == s:
        return bisect_right(arr, arr[mid]) - bisect_left(arr, arr[mid])

    # s값이 상근이의 카드 최솟값보다 작거나 최댓값보다 크다면 0개
    if arr[start] > s or arr[end] < s:
        return 0
    else:
        if arr[mid] > s:
            return card_count(arr, start, mid - 1, s)
        else:
            return card_count(arr, mid + 1, end, s)


for s in sample:
    print(card_count(cards, start, end, s), end=" ")