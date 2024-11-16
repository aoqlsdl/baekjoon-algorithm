t = int(input())

for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    # 최대 가격 초기화
    maxPrice = 0

    # 이익 초기화
    profit = 0

    for i in range(len(price) - 1, -1, -1):
        if maxPrice < price[i]:
            maxPrice = price[i]
        else:
            profit += maxPrice - price[i]

    print(profit)