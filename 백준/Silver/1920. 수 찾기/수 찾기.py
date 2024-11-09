n = int(input())
arr = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

arr.sort()

start = 0
end = n - 1

def is_included(arr, start, end, c):
    mid = int((start + end) // 2)

    if arr[mid] == c:
        return 1
    else:
        if arr[start] > c:
            return 0
        elif arr[end] < c:
            return 0

        if arr[mid] > c:
            return is_included(arr, start, mid - 1, c)
        elif arr[mid] < c:
            return is_included(arr, mid + 1, end, c)


for c in check_list:
    print(is_included(arr, start, end, c))
