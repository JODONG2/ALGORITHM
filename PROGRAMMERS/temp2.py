import heapq
def dijkstra(graph,start,goal,gates,summits,n):
    q = []
    heapq.heappush(q,([0],start))
    distance = [[float('inf')] for _ in range(n+1)]
    distance[start] = [0] 
    while q : 
        dist,now = heapq.heappop(q)
        if max(dist) > max(distance[now]):
            continue 
        for nex,d in graph[now]:
            if nex != goal and nex in summits:
                continue 
            if nex in gates :
                continue 
            temp = dist[:]
            temp.append(d)
            if max(distance[nex]) > max(temp):
                distance[nex]= temp[:]
                heapq.heappush(q,(distance[nex],nex))
    ret = 0
    for d in distance[goal]:
        if d != float('inf'):
            ret = max(ret,d)
    print(distance)
    print(goal,ret)
    return ret, goal 
def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    for start,end,dist in paths : 
        graph[start].append((end,dist))
        graph[end].append((start,dist))
    mini = float('inf')
    last = 0
    for gate in gates:
        for summit in summits:
            inten,summ = dijkstra(graph,gate,summit,gates,summits,n)
            if mini > inten : 
                mini = inten
                last = summ 
            
    return [last,mini]

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],[5]))

print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3, 7],[1, 5]))