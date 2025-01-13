# 3273. 두 수의 합

# 기준: 두 수 중 더 작은/큰 수? --> 얘를 기준으로 고정하여 범위를 정할 수 있으니까. 여기서는 더 큰 수인 e를 기준으로 함.
n = int(input())
l = list(map(int, input().split()))
x = int(input())

l.sort()

s = 0  # 시작 idx
e = n - 1  # 끝 idx

cnt = 0  # l[s] + l[e] == x 개수

while True:
    if s >= e:
        break

    if l[s] + l[e] == x:
        cnt += 1
        s += 1
        e -= 1
    # 둘이 더한 값이 x를 초과하는 순간 이후 idx는 볼 필요가 없어지므로, s는 그대로 두고, e만 한 칸 앞으로 이동
    elif l[s] + l[e] > x:
        e -= 1
    else:
        # s만 한 칸 이동, e는 가만히
        s += 1

print(cnt)