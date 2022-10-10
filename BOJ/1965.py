
cnt = int(input()) 
box_seq = list(map(int,input().split()))
dp = [1 for _ in range(cnt)]
for i in range(cnt):
    for j in range(i+1,cnt):
        if box_seq[i] < box_seq[j] :
            dp[j] = max(dp[j], dp[i]+1)
print(max(dp))
