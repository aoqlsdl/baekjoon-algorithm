t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    maxPrice = 0
    profit = 0

    for i in range(n - 1, -1, -1):
        if prices[i] > maxPrice:
            maxPrice = prices[i]
        else:
            profit += maxPrice - prices[i]

    print(f"#{_+1} {profit}")