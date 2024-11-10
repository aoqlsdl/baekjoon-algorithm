x = int(input())
arr = []

for _ in range(x):
    location = list(map(int, input().split()))
    arr.append(location)

arr.sort(key=lambda x:(x[0], x[1]))

for a in arr:
    print(a[0], a[1])