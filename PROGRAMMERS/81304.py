import heapq 
def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for x,y,d in roads :
        if x in traps or y in traps :
            graph[x].append([y,d,x])
            graph[y].append([x,d,x])
        
        else : 
            graph[x].append([y,d,-1])
            
    q = []
    heapq.heappush(q,(0,start))
    distance = [ [float('inf'),float('inf')] for _ in range(n+1)]
    distance[start][0] = 0 
    while q :
        dist, e = heapq.heappop(q)
        print(dist,e)
        if distance[e][0] < dist and distance[e][1] < dist:
            continue 
        for i,(dest,d,c) in enumerate(graph[e]) :
            if e in traps  : 
                if c != e : 
                    graph[e][i][2] = e 
                    for j,(dest2,d2,c2) in enumerate(graph[dest]):
                        if dest2 == e : 
                            graph[dest][j][2] = dest2
                    if distance[dest][0] > d+dist :
                        distance[dest][1] = distance[dest][0]
                        distance[dest][0] = d+dist
                        heapq.heappush(q,(distance[dest][0],dest))
                    elif distance[dest][1] > d+dist :
                        distance[dest][1] = d+dist
                        heapq.heappush(q,(distance[dest][1],dest))
                elif c == e : 
                    graph[e][i][2] = dest
                    # for j,(dest2,d2,c2) in enumerate(graph[dest]):
                    #     if dest2 == e : 
                    #         graph[dest][j][2] = dest2
            else :
                if c!=e:
                    continue
                if dest in traps : 
                    if distance[dest][0] > d+dist : 
                        distance[dest][1] = distance[dest][0]
                        distance[dest][0] = d+dist 
                        heapq.heappush(q,(distance[dest][0],dest))    
                    elif distance[dest][1] > d+ dist:
                        distance[dest][1] = d+dist 
                        heapq.heappush(q,(distance[dest][1],dest))         
    answer = min(distance[end])
    print(distance)
    return answer

solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])
solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3])
solution(5, 1, 5, [[1, 2, 1], [2, 3, 1], [3, 2, 1], [3, 5, 1], [1, 5, 10]],[5])