import heapq

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

def findCheapestPrice(n, flights, src, dst, k):
    graph = {}
    for s, d, w in flights:
        if s not in graph:
            graph[s] = [(d,w)]
        else:
            graph[s].append((d,w))
            
    pq = [(0, src, k+1)]
    vis = [0] * n
    
    while pq:
        w, x, K = heapq.heappop(pq)
        if x == dst:
            return w
        if vis[x] >= K:
            continue
        vis[x] = K
        if x in graph:
            for y, dw in graph[x]:
                heapq.heappush(pq, (w+dw, y, K-1))
    return -1

ans = findCheapestPrice(n, flights, src, dst, k)
print(ans)