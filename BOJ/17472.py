import sys 
from collections import deque 
import heapq 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def grouping(board,visit,i,j,id):
    q = deque() 
    q.append((i,j))
    while q : 
        x,y = q.popleft() 
        for d in range(4):
            nx = x+dx[d] 
            ny = y+dy[d] 
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] and board[nx][ny] == 1:
                board[nx][ny] = id 
                visit[nx][ny] = False 
                q.append((nx,ny))
                land_pos.append((nx,ny))

def cal_dist(graph,board,i,j):
    for d in range(4):
        nx = i + dx[d] 
        ny = j + dy[d] 
        dist = 0 
        while 0<=nx<n and 0<=ny<m and board[nx][ny] == 0 :
            nx+= dx[d] 
            ny+= dy[d] 
            dist +=1 
            if 0<=nx<n and 0<=ny<m and board[nx][ny] != 0 and dist != 1:
                graph[board[i][j]-1][board[nx][ny] -1] = min(graph[board[i][j]-1][board[nx][ny]-1] , dist)
                graph[board[nx][ny]-1][board[i][j]-1] = graph[board[i][j]-1][board[nx][ny]-1] 
    

def mst(graph,land_num):
    pq = []
    heapq.heappush(pq,(0,0)) 
    ret = 0 
    visit = [False for _ in range(land_num)]
    cnt = 0 
    while pq : 
        dist, now = heapq.heappop(pq) 
        if visit[now] : continue 
        ret += dist       
        visit[now] = True 
        cnt+=1 
        if cnt == land_num : return ret 
        for i in range(land_num):
            if not visit[i] and graph[now][i] != float('inf'): 
                heapq.heappush(pq,(graph[now][i],i)) 
    return -1 


if __name__ =="__main__":
    n,m = map(int,sys.stdin.readline().split()) 
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 
    land_num = 1 
    visit = [[True for _ in range(m)] for _ in range(n)]
    land_pos = [] 
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and visit[i][j]:
                visit[i][j] = False 
                board[i][j] = land_num 
                grouping(board,visit,i,j,land_num)
                land_num += 1
                land_pos.append((i,j))

    graph = [[float('inf') for _ in range(land_num-1)] for _ in range(land_num-1)]

    for i,j in land_pos:
        if board[i][j] != 0 :
            cal_dist(graph,board,i,j)

    ans = mst(graph,land_num-1) 
    print(ans)
