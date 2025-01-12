n = int(input())
weights = []

for i in range(n):
    w = int(input())
    weights.append(w)

weights.sort()
heaviest_weights = []

for i in range(n):
    heaviest_weight = (n - i) * weights[i]
    heaviest_weights.append(heaviest_weight)

heaviest_weights.sort(reverse=True)

heaviest_w = heaviest_weights[0]

print(heaviest_w)