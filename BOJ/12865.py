#https://www.acmicpc.net/problem/12865
#knapsack 알고리즘

N, K = map(int,input().split()) 
item = [[0,0]]
pack = [[0 for _ in range(K+1)] for _ in range(N+1)] 
for _ in range(N):
    item.append(list(map(int,input().split()))) # [w, v]
for n in range(1,N+1):
    for k in range(1,K+1):
        weight = item[n][0]
        value = item[n][1] 
        if weight > k : 
            pack[n][k] = pack[n-1][k] 
        else : 
            pack[n][k] = max(value + pack[n-1][k - weight], pack[n-1][k])
print(pack[-1][-1])
            
    
