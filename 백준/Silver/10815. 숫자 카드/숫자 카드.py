# 10815. 숫자 카드
import sys

# 상근이가 가진 숫자 카드
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 정렬
n_arr.sort()

# 주어진 숫자 카드
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, start, end, elem):
    mid = (start + end) // 2

    # mid == elem이면 1 반환
    if arr[mid] == elem:
        return 1

    # 더이상 탐색할 원소가 없거나 arr의 최대/최솟값보다 크거나 작으면 0 반환
    if start == end or elem > arr[end] or elem < arr[start]:
        return 0

    # mid != elem이면 재귀함수
    if arr[mid] > elem:
        return binary_search(arr, start, mid - 1, elem)
    elif arr[mid] < elem:
        return binary_search(arr, mid + 1, end, elem)

for elem in m_arr:
    print(binary_search(n_arr, 0, n - 1, elem), end=" ")