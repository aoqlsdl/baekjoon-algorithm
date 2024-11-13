n = int(input())
results = []

for i in range(n // 5 + 1):
    result = 0
    cal = 5 * i

    if cal == n:
        result += i
    elif (n - cal) % 3 == 0:
        result += ((n - cal) // 3) + i
    elif (n - cal) % 3 != 0:
        result = -1

    results.append(result)

while -1 in results:
    results.remove(-1)

if len(results) == 0:
    print(-1)
else:
    print(min(results))
