import heapq

graph = {
    'A': {'B':1,'C':4},
    'B': {'C':2,'D':5},
    'C': {'D':1},
    'D': {}
}

def dijkstra(start):
    pq = [(0,start)]
    dist = {n:float('inf') for n in graph}
    dist[start]=0

    while pq:
        d,u = heapq.heappop(pq)
        for v,w in graph[u].items():
            if d+w < dist[v]:
                dist[v]=d+w
                heapq.heappush(pq,(dist[v],v))
    return dist

print(dijkstra('A'))
