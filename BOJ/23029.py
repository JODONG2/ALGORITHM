N = int(input()) 
food = []
dp = [0 for _ in range(N)]
for i in range(N): 
    cnt = int(input())
    if i == 0 : 
        dp[i] = [cnt]
    elif i==1:
        dp[i] = [cnt, dp[i-1][0]+cnt//2, dp[i-1][0]] 
    else : 
        dp[i] = [dp[i-1][2]+cnt, dp[i-1][0]+cnt//2, max(dp[i-1][0], dp[i-1][1],dp[i-1][2])]
print(max(dp[-1]))
         
