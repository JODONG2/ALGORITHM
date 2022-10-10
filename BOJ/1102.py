import sys 

def f(visit, cnt ):

    if cnt >= limit : 
        return 0 

    if dp[cnt][visit] != -1 : 
        return dp[cnt][visit] 

    dp[cnt][visit] = float('inf') 

    for i in range(n):
        if ((1<<i) & visit) == 0 : 
            continue 
        for j in range(n):
            if((1<<j) & visit) == 0 : 
                dp[cnt][visit] = min(dp[cnt][visit] , f((1<<j)|visit, cnt+1) + graph[i][j]) 
    return dp[cnt][visit] 

n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 

visit = 0 
cnt = 0 
for i,Y in enumerate(sys.stdin.readline()):
    if Y=='Y':
        visit |= 1<<(i)
        cnt+=1 
limit = int(sys.stdin.readline()) 
dp = [[-1 for _ in range(1<<n)] for _ in range(n)]
ans = f(visit,cnt)
if ans == float('inf') : ans = -1 
print(ans)
