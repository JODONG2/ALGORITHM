if __name__ =="__main__":
    N = int(input()) 
    dp = [0 for _ in range(N)]
    for i in range(N): 
        food = int(input()) 
        if i == 0: 
            dp[i] = [food]
        elif i == 1 : 
            dp[i] = [dp[i-1][0], dp[i-1][0]+food//2, food ] #현재 안먹음, 연속으로 먹음, 저번꺼안먹었고 이번거 먹음 
        else : 
            dp[i] = [max(dp[i-1]), dp[i-1][2]+food//2, dp[i-1][0]+food]
    print(max(dp[-1]))
    

























# N = int(input()) 
# food = []
# dp = [0 for _ in range(N)]
# for i in range(N): 
#     cnt = int(input())
#     if i == 0 : 
#         dp[i] = [cnt]
#     elif i==1:
#         dp[i] = [cnt, dp[i-1][0]+cnt//2, dp[i-1][0]] 
#     else : 
#         dp[i] = [dp[i-1][2]+cnt, dp[i-1][0]+cnt//2, max(dp[i-1][0], dp[i-1][1],dp[i-1][2])]
# print(max(dp[-1]))


         
