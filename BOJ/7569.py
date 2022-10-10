import sys
from collections import deque 
M,N,H = map(int,input().split()) 

box = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dx = [0,0,0,0,1,-1]
dy = [1,-1,0,0,0,0]
dz = [0,0,1,-1,0,0]
check = [[[True for _ in range(M)] for _ in range(N)] for _ in range(H)] 
start = deque() 
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1 : 
                start.append((i,j,k,0))
                check[i][j][k] = False 
            elif box[i][j][k] == -1:
                check[i][j][k] = False 

def bfs():
    q = deque(start)
    time = 0 
    while q : 
        x,y,z,time = q.popleft() 
        for px,py,pz in zip(dx,dy,dz):
            nx,ny,nz = x+px,y+py,z+pz 
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and check[nx][ny][nz] :  
                check[nx][ny][nz] = False 
                q.append((nx,ny,nz,time+1))
    return time 
answer = bfs() 
for ch in check:
    for c in ch :
        if any(c):
            answer = -1 
            break 
    if answer == -1:
        break 
print(answer) 


""""
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

"""