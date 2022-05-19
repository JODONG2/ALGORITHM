

import sys 
import heapq 
def prim():
    q = [] 
    heapq.heappush(q,(0,1))
    visit = [True for _ in range(n+1)]
    visit[0] = False 
    ret = 0
    while q : 
        if not any(visit):
            break 
        cost,now = heapq.heappop(q) 
        if visit[now] : 
            visit[now] = False 
            ret+= cost  
            for next,loss in graph[now]:
                heapq.heappush(q,(loss,next)) 
    return ret 

n,m = map(int,sys.stdin.readline().split()) 
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,t = map(int,sys.stdin.readline().split()) 
    graph[x].append((y,t))
    graph[y].append((x,t))
print(prim())
"""
3 3
1 2 1
2 3 2
1 2 -100

3 3
1 2 1
2 3 2
1 3 3
"""