
ans = float("inf")

def input_data():
    n = int(input()) 
    s = [list(map(int,input().split())) for _ in range(n)]
    return n, s 

def div_team (idx,cnt,n,s,team):
    global ans 
    if cnt == n//2 :
        start , link = 0,0 
        for i in range(n): 
            for j in range(n):
                if team[i] and team[j] :
                    start+= s[i][j]
                elif not team[i] and not team[j] :
                    link += s[i][j] 
        ans = min(ans , abs(start-link))
    
    for i in range(idx,n):
        if team[i] :
            continue 
        team[i] = 1 
        div_team(i+1, cnt+1, n, s, team)
        team[i] = 0 
    

if __name__ == "__main__":
    n,s = input_data()
    team = [0 for _ in range(n)]
    div_team(0,0,n,s,team)
    print(ans)