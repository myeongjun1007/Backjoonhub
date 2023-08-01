import sys
from collections import deque
sys.setrecursionlimit(100000)

N,M,V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    v1 , v2 = map(int,sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(len(graph)):
    graph[i].sort()

def bfs(start):
    que = deque()
    visited = [0 for _ in range(N+1)]
    que.append(start)
    visited[start] =1

    while len(que) > 0 :
        curr = que[0]
        print(curr, end=' ')
        for next in graph[curr]:
            if visited[next] == 0:
                visited[next] = 1
                que.append(next)

        que.popleft()

visited_dfs = [0 for _ in range(N+1)]

def dfs(n):
    print(n, end=' ')
    visited_dfs[n] = 1

    for next in graph[n]:
        if visited_dfs[next] == 0:
            visited_dfs[next] = 1
            dfs(next)

dfs(V)
print()
bfs(V)