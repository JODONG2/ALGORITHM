import sys 
from collections import deque 

def find_path(dp,graph,start2,go_in):
    q = deque(start2)
    while q :
        start = q.popleft()
        for g in graph[start]:
            finish = g
            dp[finish] = max(dp[finish] , dp[start]+time[finish])
            go_in[finish] -= 1 
            if go_in[finish] == 0 :
                q.append(finish)

T = int(sys.stdin.readline())
for t in range(1,T+1):
    answer = 0 
    n,k = map(int,sys.stdin.readline().split())
    graph = [ []for _ in range(n) ]
    go_in = [0 for _ in range(n)]
    time = list(map(int,sys.stdin.readline().split())) 
    for _ in range(k):
        IN,OUT = map(int,sys.stdin.readline().split()) 
        graph[IN-1].append(OUT-1)
        go_in[OUT-1] +=1 
    dp = [0 for _ in range(n)]
    start = []
    for i in range(n):
        if go_in[i] == 0 : 
            dp[i] += time[i]
            start.append(i)
    target = int(sys.stdin.readline())
    find_path(dp,graph,start,go_in)
    answer = dp[target-1]
    print(f"{answer}")