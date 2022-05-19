"""
2
7 5
0 1 2
1 3 4
0 2 1
0 4 3
3 2 3
3 4 4
2 4 1
3 5
0 1 2
1 3 4
4 2 1
"""
import sys 
import heapq 
def dijkstra(start,end):
    q = [] 
    visit = [[] for _ in range(m)]
    heapq.heappush(q,(0,start))
    visit[0].append(start)
    conn = [float('inf')] * m
    conn[0] = 0 
    while q : 
        point, now  = heapq.heappop(q)
        if conn[now] < point : 
            continue 
        for next,p in graph[now]: 
            if conn[next] > point+p : 
                conn[next] = point+p 
                visit[next] = []
                for v in visit[now]:
                    visit[next].append(v)
                visit[next].append(next)
                heapq.heappush(q,(conn[next],next))
    return visit[m-1]

tc = int(sys.stdin.readline())
for t in range(1,tc+1):
    n,m = map(int,sys.stdin.readline().split()) 
    graph = [[] for _ in range(m)] 
    for _ in range(n):
        n,c,point = map(int,sys.stdin.readline().split()) 
        graph[n].append((c,point))
        graph[c].append((n,point))
    answer = dijkstra(0,m-1)
    if not answer: 
        answer = - 1
        print(f"Case #{t}: {answer}")
    else: 
        print(f"Case #{t}: ",end = '')
        for a in answer : 
            print(a,end=' ')
        print()

