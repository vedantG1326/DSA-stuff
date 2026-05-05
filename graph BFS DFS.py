graph = {
    'A': ['B','C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

# BFS
from collections import deque
def bfs(start):
    q = deque([start])
    visited = set()
    while q:
        n = q.popleft()
        if n not in visited:
            print(n, end=" ")
            visited.add(n)
            q.extend(graph[n])

# DFS
def dfs(n, visited=set()):
    if n not in visited:
        print(n, end=" ")
        visited.add(n)
        for i in graph[n]:
            dfs(i, visited)

bfs('A')
print()
dfs('A')
