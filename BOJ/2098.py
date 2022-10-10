import sys 
import time 
inf = float('inf')

def dfs(now,visit):
    if visit == (1<<n) -1 : 
        if graph[now][0] :
            return graph[now][0] 
        else :
            return inf

    if dp[now][visit] != -1 : 
        return dp[now][visit] 
    temp = inf 
    
    for i in range(1,n):
        if not graph[now][i]: 
            continue
        if visit & (1 << i) : 
            continue 
        temp = min(temp, dfs(i, visit|(1<<i)) + graph[now][i])
    dp[now][visit] = temp 
    return dp[now][visit]

n = int(sys.stdin.readline()) 
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 
start = time.time() 
# start 0 
# end   0
dp = [[-1 for _ in range(1<<n)] for _ in range(n)] 
print(dfs(0,1))
print(time.time()- start)
for d in dp :
    print(d) 
