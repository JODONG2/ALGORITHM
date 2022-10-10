import sys 
from collections import deque 
s,e = map(int,sys.stdin.readline().split()) 
dp = [[float('inf'),0] for _ in range(max(e,s)*2+2)] 
dp[s][0] = 0 
dp[s][1] = 1  
q = deque([(s,0)])
ans = 0 
mini = float('inf')
while q : 
    now,t = q.popleft()
    if now == e : 
        continue 
    if dp[e][0] < t :
        continue
    if dp[now][0] < t : 
        continue 
    if now > e: 
        if dp[now - 1][0] > t+1 : 
            dp[now-1][0] = t+1 
            dp[now-1][1] = max(dp[now][1],1)
            q.append((now-1,t+1))
        elif dp[now-1][0] == t+1 : 
            dp[now-1][1] += max(1,dp[now][1])
    elif now < e : 
        if dp[now+1][0] > t+1 : 
            dp[now+1][0] = t+1 
            dp[now+1][1] = max(dp[now][1],1) 
            q.append((now+1,t+1))
        elif dp[now+1][0] == t+1 :
            dp[now+1][1] += max(1,dp[now][1])
        
        if 0 < now and dp[now-1][0] > t+1 : 
            dp[now-1][0] = t+1 
            dp[now-1][1] = max(dp[now][1],1)
            q.append((now-1,t+1))
        elif 0<now and dp[now-1][0] == t+1 : 
            dp[now-1][1] += max(1,dp[now][1])
        
        if dp[now * 2][0] > t+1 : 
            dp[now*2][0] = t+1 
            dp[now*2][1] = max(dp[now][1],1)
            q.append((now*2,t+1))
        elif dp[now*2][0] == t+1 : 
            dp[now*2][1] += max(1,dp[now][1])
for ans in dp[e] : 
    print(ans) 