import sys

def dfs():
    if len(s) == m:
        # m자리 숫자가 되면 리스트를 합쳐서 출력 후 되돌아가기
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1): # 1부터 n까지 순회 (첫 번째 자리)
        if visited[i]: # 이미 살펴본 수라면 패스
            continue

        # 방문 처리 후 리스트에 추가
        visited[i] = 1
        s.append(i)

        # 다음 자리수로 이동
        dfs()

        # s에서 요소를 하나씩 빼내기
        s.pop()

        # s를 빼냈기 때문에 방문 취소
        visited[i] = 0
            

input = sys.stdin.readline
n, m = map(int, input().split())
s = []
visited = [0] * (n + 1)

dfs()