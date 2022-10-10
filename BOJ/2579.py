import sys

if __name__ == "__main__": 
    N = int(input()) 
    if N == 1 : 
        print(int(input()))
    else:
        dp = [0 for _ in range(N)]
        for i in range(N):
            point = int(input())
            if i == 0 : 
                dp[i] = [point]
            elif i == 1 : 
                dp[i] = [dp[i-1][0], dp[i-1][0]+point, point] #안밟음, 전꺼랑 연속해서 밟음, 전전꺼에서 밞음
            else :
                dp[i] = [max(dp[i-1][1:]), dp[i-1][2]+point, dp[i-1][0]+point] 
        print(max(dp[-1][1], dp[-1][2]))
        
            
"""

6
10
20
15
25
10
20

5
5
4
3
2
1

6
123
14
3
2
13
4

답 143
"""