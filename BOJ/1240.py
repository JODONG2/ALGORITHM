import sys 
import heapq 
nodes,targets = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(nodes+1)]
for _ in range(nodes-1) : 
    start,end,cost = map(int,sys.stdin.readline().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

distance = [[float('inf') for _ in range(nodes+1)]for _ in range(nodes+1)]
def dijkstra(start,target):
    if not distance[start][start] != float('inf') :
        q = [] 
        heapq.heappush(q,(0,start)) 
        distance[start][start] = 0 
        while q : 
            D,NEXT = heapq.heappop(q) 
            if distance[start][NEXT] < D : 
                continue 
            for dest,dist in graph[NEXT] : 
                if D+dist < distance[start][dest] : 
                    distance[start][dest] = D+dist 
                    heapq.heappush(q,(distance[start][dest], dest))
    return distance[start][target]

for _ in range(targets):
    start,target = map(int,sys.stdin.readline().split()) 
    print(dijkstra(start,target))

