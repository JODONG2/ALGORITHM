import sys 

if __name__ == "__main__": 
    n,k = map(int,input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(k+1)]
    dp[0]= 1 
    for coin in coins : 
        for d in range(coin,k+1): 
            dp[d] += dp[d-coin]
        