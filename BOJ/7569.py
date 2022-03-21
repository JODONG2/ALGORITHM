import sys
from copy import deepcopy
N,M,H = map(int,input().split()) 

box = [[list(map(int,sys.stdin.readline().split())) for _ in range(M)] for _ in range(H)]

dx = [0,0,0,0,1,-1]
dy = [1,-1,0,0,0,0]
dz = [0,0,1,-1,0,0]
def dfs(boxes,answer):
    copy_box = []
    copy_box = deepcopy(boxes)
    cheat = []
    for h in range(H):
        for m in range(M):
            for n in range(N):
                if boxes[h][m][n] == 0 : 
                    fail = True 
                    for px,py,pz in zip(dx,dy,dz):
                        nx,ny,nz = n+px, m+py, h+pz 
                        if 0<=nx<N and 0<=ny<M and 0<=nz<H and not boxes[nz][ny][nx] == -1:
                            fail = False 
                            break
                    if fail : 
                        return -1 
                elif boxes[h][m][n] == 1 : 
                    for px,py,pz in zip(dx,dy,dz):
                        nx,ny,nz = n+px, m+py, h+pz 
                        if 0<=nx<N and 0<=ny<M and 0<=nz<H and boxes[nz][ny][nx] == 0:
                            copy_box[nz][ny][nx] = 1
                            cheat.append([nz,ny,nx])
    if boxes == copy_box or not cheat :
        return 0 
    boxes = copy_box
    answer += 1 
    
    while True :
        copy_box = deepcopy(boxes)
        copy_cheat = cheat
        cheat = [] 
        for ch in copy_cheat : 
            z,y,x = map(int,ch)
            for px,py,pz in zip(dx,dy,dz):
                nx,ny,nz = x+px, y+py, z+pz 
                if 0<=nx<N and 0<=ny<M and 0<=nz<H and boxes[nz][ny][nx] == 0:
                    copy_box[nz][ny][nx] = 1
                    cheat.append([nz,ny,nx])
        if copy_box == boxes or not cheat :
            break 
        else : 
            boxes = copy_box
            answer += 1
            del copy_box
    return answer 

print(dfs(box,0))
    
""""
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

"""