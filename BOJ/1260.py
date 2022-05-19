import sys 
from collections import deque 
N,M,V = map(int,sys.stdin.readline().split()) 
graph = [[] for _ in range(N+1)] 
for _ in range(M):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start) 

def dfs (start,visit):
    graph[start].sort()
    for dest in graph[start]:
        if not dest in visit:
            visit.append(dest)
            dfs(dest,visit)
def bfs(start,visit):
    q= deque()
    q.append(start) 
    while q : 
        s = q.popleft() 
        graph[s].sort()
        for g in graph[s] : 
            if not g in visit : 
                visit.append(g)
                q.append(g)
    
visit_dfs = [V]
dfs(V,visit_dfs)
print(' '.join(map(str,visit_dfs)))
visit_bfs = [V]
bfs(V,visit_bfs)
print(' '.join(map(str,visit_bfs)))

