import sys 
import heapq 

def dijkstra(s):
    q = [] 
    heapq.heappush(q,(0,s))
    while q : 
        dist,now = heapq.heappop(q) 
        if distance[now] < dist :
            continue 
        for n,d in graph[now] : 
            if dist+d < distance[n]: 
                distance[n] = dist+d 
                heapq.heappush(q,(distance[n],n))
    

n  = int(sys.stdin.readline()) 
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)] 
for _ in range(m):
    s,e,d = map(int,sys.stdin.readline().split())
    graph[s].append((e,d))

v1,v2 = map(int,sys.stdin.readline().split()) 
distance = [float('inf') for _ in range(n+1)] 
distance[v1] = 0 
dijkstra(v1) 
print(distance[v2])

