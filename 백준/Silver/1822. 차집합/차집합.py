nA, nB = map(int, input().split())

# set -> 집합이니까 차집합 구하기 가능
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 차집합
result = sorted(list(A - B))

print(len(result))
for r in result:
    print(r, end=" ")