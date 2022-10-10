import sys 

tc = int(sys.stdin.readline())
for _ in range(tc):
    city,air = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(city+1)] 
    visited = [False for _ in range(city+1)]
    for _ in range(air): 
        _,_ = map(int,sys.stdin.readline().split())
        # s,e = map(int,sys.stdin.readline().split()) 
        # graph[s].append(e)
        # graph[e].append(s)
    print(city-1)