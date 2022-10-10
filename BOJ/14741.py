import sys 
from collections import deque 
point = float('inf') 

def isConnTeamB(teamA):
    # visit = teamA[:]
    visit = teamA
    teamB = deque() 
    for i in range(n) : 
        if (teamA & (1<<i)) == 0: 
            teamB.append(i)
            break
    last = (1<<n) -1
    while teamB:
        now = teamB.popleft()
        if (visit & (1<<now)) != 0 : 
            continue 

        visit |= 1<<now 
        if visit == last : 
            return True 

        for i in range(n) : 
            if (visit & 1<<i)== 0 and city_conn[now][i] == 1:
                teamB.append(i)
    return False 

def comb(teamA_point, teamA,q):
    if dp[teamA] : return 
    dp[teamA] = True 
    global point 
    if point == 0 : 
        return 
    if abs(total - teamA_point - teamA_point) < point and isConnTeamB(teamA):
        point = abs(total-teamA_point - teamA_point)
    
    for i in q : 
        if (teamA & 1<<i) != 0 : continue 
        teamA_point+= city_cnt[i] 
        temp = q[:]
        for j in range(n):
            if city_conn[i][j] != 0 and (teamA & 1<<j) == 0 :
                temp.append(j)
        comb(teamA_point, teamA | 1<<i, temp)
        if point == 0 : return 
        teamA_point -= city_cnt[i]

n = int(sys.stdin.readline()) 
dp = [False for _ in range(2**n)]
city_cnt = list(map(int,sys.stdin.readline().split()))
total = sum(city_cnt) 

city_conn = [[0 for _ in range(n)] for _ in range(n)]  # -1해야댐

for i in range(n): 
    infor = list(map(int,sys.stdin.readline().split())) 
    for j in range(1,len(infor)): 
        city_conn[i][infor[j]-1] = 1

teamA_point = city_cnt[0]

comb(teamA_point,1 , [i for i in range(n) if city_conn[0][i] == 1])
print(-1 if point == float('inf') else point)



"""

9
1 2 3 4 5 6 7 8 9
2 2 4
4 1 3 5 4
4 2 5 8 7
4 6 9 1 2
2 2 3
1 4
1 3
1 3
1 4

답 1 (3, 5, 7, 8 / 1, 2, 4, 6, 9)

6
2 2 2 2 2 2
1 3
1 4
1 1
1 2
1 6
1 5

5 
5 2 3 4 1 
1 2 
4 1 3 5 4 
1 2 
1 2
1 2

3 
1 2 1 
1 2 
2 1 3 
1 2

8
17 42 46 81 71 8 37 12
4 2 4 5 7
5 1 3 4 5 8
2 2 4
5 1 2 3 7 8
5 1 2 6 7 8
2 5 8
4 1 4 5 8
5 2 4 5 6 7
"""

