from bisect import bisect_left

n = int(input())
x_list = list(map(int, input().split()))
sorted_x_list = sorted(list(set(x_list)))

for x in x_list:
    # x에 대해 x보다 작은 값은 x보다 왼쪽에 있는 숫자들의 수를 출력
    print(bisect_left(sorted_x_list, x), end=" ")