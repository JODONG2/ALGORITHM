if __name__ == "__main__":
    n = int(input()) 

    seq = list(map(int,input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = 0
    for num in range(n) :
        for comp in range(num): 
            if seq[num] > seq[comp] and dp [num] < dp[comp]: 
                dp[num] = dp[comp] 
        dp[num] += 1 

    print(max(dp))