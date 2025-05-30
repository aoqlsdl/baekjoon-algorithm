from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)

if s == g:
    print(0)
    exit()

q = deque()
q.append((s, 0))
visited[s] = 1

while q:
    x, cnt = q.popleft()

    for nx in (x + u, x - d):
        if 1 <= nx <= f and not visited[nx]:
            if nx == g:
                print(cnt + 1)
                exit()
            visited[nx] = 1
            q.append((nx, cnt + 1))

print("use the stairs")
