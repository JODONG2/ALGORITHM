"""
3 9
XXXXXXXXX
A.......B
XXXX.XXXX
"""
import sys 
from collections import deque 
dx=[0,0,0,1,1,1,-1,-1,-1]
dy=[1,0,-1,1,0,-1,1,0,-1]
def change_position(a_position,b_position):
    q = deque() 
    ax,ay = a_position[0]
    bx,by = b_position[0]
    q.append((ax,ay,bx,by,0)) 
    visit = [[[[True for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visit[ax][ay][bx][by] = False 
    while q : 
        ax,ay,bx,by,time = q.popleft()
        for px,py in zip(dx,dy): 
            nax,nay = ax+px, ay+py 
            if 0<=nax<n and 0<=nay<m and maps[nax][nay] != 'X':
                for px,py in zip(dx,dy): 
                    nbx,nby = bx+px, by+py  
                    if 0<=nbx<n and 0<=nby<m and maps[nbx][nby] != 'X': 
                        if visit[nax][nay][nbx][nby] : 
                            if (nbx==nax and nby==nay) : #같은 위치로 이동 
                                continue 
                            if nax==bx and nay == by and nbx == ax and nby == ay: #교차 
                                continue 
                            if (nax,nay) == b_position[0] and (nbx,nby) == a_position[0] : # 성공
                                return time+1
                            visit[nax][nay][nbx][nby] = False 
                            q.append((nax,nay,nbx,nby,time+1))
    return -1 

def find_position():
    ret_a = [] 
    ret_b = []
    for i in range(n):
        for j in range(m): 
            if maps[i][j] == 'A' : 
                ret_a.append((i,j)) 
            elif maps[i][j] == 'B' : 
                ret_b.append((i,j))
            if ret_a and ret_b : 
                return ret_a,ret_b


n,m = map(int,sys.stdin.readline().split()) 
maps = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
a_position, b_position = find_position()
print(change_position(a_position,b_position))