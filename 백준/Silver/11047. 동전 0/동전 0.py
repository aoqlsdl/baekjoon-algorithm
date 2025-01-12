n, k = map(int, input().split())
coins = []
cnt = 0

for i in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

for coin in coins:
    if k == 0:
        break
    else:
        if coin > k:
            continue
        else:
            cnt += k // coin
            k %= coin
print(cnt)