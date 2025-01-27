# 11725. 트리의 부모 찾기
import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
trees = [{"conn": [], "parent": [], "children": []} for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().split())

    # 딕셔너리에 연결노드로 우선 저장해두기
    trees[n1]['conn'].append(n2)
    trees[n2]['conn'].append(n1)

def recursive_func(v):
    if v == 1:
        trees[v]['parent'].append(0)

    for c in trees[v]['conn']:
        if c != trees[v]['parent'][0]: # 연결 노드가 부모 노드가 아닐 경우에는 무조건 자식 노드
            trees[v]['children'].append(c)

    for c in trees[v]['children']:
        trees[c]['parent'].append(v)
        recursive_func(c) # 자식 노드를 타고 들어가서 동일한 과정 반복


# 1번부터 순회하면서 부모-자식 관계 매핑
recursive_func(1)


for i in range(2, n + 1):
    print(trees[i]['parent'][0])
