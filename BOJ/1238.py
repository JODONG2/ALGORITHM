import sys 
import heapq 
n,m,target = map(int,sys.stdin.readline().split()) #N개 마을, M개 도로, X 목적지 
graph= [[] for _ in range(n)]
target -= 1
for _ in range(m):
    x,y,time = map(int,sys.stdin.readline().split())
    x-=1 
    y-=1 
    graph[x].append((y,time))

def dijkstra(start,goal):
    q = [] 
    distance=[float('inf') for _ in range(n)] 
    distance[start] = 0 
    heapq.heappush(q,(0,start)) 

    while q :
        dist,now = heapq.heappop(q)
        if distance[now] < dist : 
            continue 
        for dest,d in graph[now]: 
            if distance[dest] > d + dist :
                distance[dest] = d+dist 
                heapq.heappush(q,(distance[dest],dest))
    return distance[goal]
answer = 0 

for i in range(n):
    if i == target:
        continue 
    answer = max(answer, dijkstra(i,target)+dijkstra(target,i))
print(answer)

