# idea: 가장 큰 숫자를 pop해서 n번째로 큰 수를 찾으면 된다.
n = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

result = 0

arr_A.sort()

for i in range(n):
    b_max = max(arr_B)
    result += arr_A[i] * b_max
    arr_B.remove(b_max)

print(result)