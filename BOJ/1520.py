#내리막길

#TODO: 주변 작은수 찾기 (상하좌우)
"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
"""

def input_road() -> list:
    N,M = map(int, input().split())
    road = []
    for _ in range(N):
        road.append(list(map(int,input().split())))
    return road,N,M

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def search_path(x,y) :
    if dp[x][y] != -1 :
        return dp[x][y] 
    if [x,y] == [N-1,M-1]:
        return 1
    
    dp[x][y] = 0 
    for d in range(4):
        nx = x+dx[d] 
        ny = y+dy[d] 
        if 0<=nx<N and 0<=ny<M : 
            if road[nx][ny] < road[x][y] : 
                dp[x][y] += search_path(nx,ny)
    return dp[x][y]
        
    
if __name__=="__main__":
    road,N,M = input_road()
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    print(search_path(0,0))

    
"""

4 4
16 9 8 1
15 10 7 2
14 11 6 3
13 12 5 4

"""