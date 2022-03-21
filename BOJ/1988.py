import sys 
#실패;
N, b = map(int,input().split())
dp = [0 for _ in range(N)] 
times = [int(sys.stdin.readline()) for _ in range(N)]

for i in range(N): 
    if i == 1 : 
        dp[i] = [0,b]
    elif i == 2 : 
        dp[i] = [[0,0],[times[i],b-1]]
    else : 
        dp[i] = [[0,0],[times[i],dp[i-1][1][1]-1],]

