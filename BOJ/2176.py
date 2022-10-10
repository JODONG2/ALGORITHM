"""
4 4
1 3 1
3 2 2
1 4 2
2 4 1

6 7
1 2 10 
1 3 1
3 2 1 
1 4 1
4 2 1
1 5 1 
5 2 1 

6 7
1 2 10 
1 3 1
3 4 11 
3 5 8
4 2 1
1 5 1 
5 2 1 
"""
import sys 
# import heapq 
# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     dista = [float('inf')] * (n+1)
#     dista[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if dista[now] < dist : 
#             continue 
#         for d, next in graph[now]:
#             if d +dist < dista[next] : 
#                 dista[next]= dist+d 
#                 heapq.heappush(q, (dista[next], next))
#     return dista[2]
from collections import deque 
cnt = 0 
def search_optim(start):
    global cnt 
    if start == 2 : 
        cnt+=1 
    for d,n in graph[start] : 
        if distance[n] <= distance[start] : 
            visit[n]= False 
            search_optim(start)
            visit[n] = True 
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [float('inf') for _ in range(n+1)]
visit = [True for _ in range(n+1)]
visit[1] = False 
for _ in range(m):
    x,y,t = map(int,sys.stdin.readline().split())
    if x==2 : 
        graph[y].append((t,x))
        distance[y] = t 
        continue 
    if y == 2 : 
        graph[x].append((t,y)) 
        distance[x] = t 
        continue
    if x == 1 : 
        graph[x].append((t,y))
    elif y == 1 : 
        graph[y].append((t,x)) 
    else:
        graph[x].append((t,y))
        graph[y].append((t,x))
# value = [ 0 for _ in range(n+1)]
# for i in range(1,n+1):
#     if i == 2 :
#         continue 
#     distance[i] = dijkstra(i) 
print(distance)
search_optim(1)
print(cnt )

