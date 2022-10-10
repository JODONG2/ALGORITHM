"""
5 5 1
1 4
1 2
2 3
2 4
3 4
"""
import sys 
from collections import deque 
def bfs(s,seq):
    q = deque([s])
    
    while q : 
        now = q.popleft() 
        graph[now].sort()
        for n in graph[now]:
            if visit[n]:
                q.append(n)
                visit[n] = False 
                answer[n] = seq 
                seq+=1

n,m,start = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
seq = 2
for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
visit = [True for _ in range(n+1)]
visit[start] = False 
answer[start] = 1 
bfs(start,seq)
for ans in answer[1:]: 
    print(ans)

