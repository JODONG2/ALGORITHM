n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)] 
dp = [float("inf") for _ in range(k+1)]
dp[0] = 0 
for coin in coins:
    for d in range (coin,k+1): 
        dp[d] = min(dp[d%coin] + d//coin, dp[d], dp[d - coin]+1)
        #print(dp, coin)
answer = -1 if dp[-1] == float("inf") else dp[-1] 
print(answer)

"""
3 20
15
21
5

4
"""