"""
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......

5 5
C..**
.*.**
.*...
.***C
.....

4 6
.C..
....
....
**.*
....
...C
"""
import sys 
from collections import deque 
def bfs():
    q = deque(start[:4])
    while q : 
        x,y,cnt,d = q.popleft() 
        for d2,dir in enumerate(direction): 
            nx,ny = x+dir[0] , y+dir[1] 
            tx,ty = x+dir[0]*2 , y+dir[1]*2 
            if 0<=nx<h and 0<=ny<w and maps[nx][ny] != '*' and visit[nx][ny] > cnt:
                if d==d2:
                    visit[nx][ny] = cnt 
                    q.append((nx,ny,cnt,d2))
                else : 
                    visit[nx][ny] = cnt+1 
                    q.append((nx,ny,cnt+1,d2))
            elif 0<=tx<h and 0<=ty<w and maps[tx][ty] != '*' and visit[nx][ny] == cnt and visit[tx][ty] > cnt : 
                if d==d2:
                    q.append((tx,ty,cnt,d2))
                else: 
                    q.append((tx,ty,cnt+1,d2))

    return visit[start[4][0]][start[4][1]]

w,h = map(int,sys.stdin.readline().split())
maps = [] 
start = [] 
direction = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(h): 
    line = list(sys.stdin.readline()[:-1]) 
    for j in range(w):
        if line[j] == 'C':
            for d in range(4):
                start.append((i,j,0,d)) #x,y,mirror_cnt, direction
    maps.append(line)
visit = [[9 for _ in range(w)] for _ in range(h)] 
visit[start[0][0]][start[0][1]] = -1 
print(bfs())
# for v in visit:
#     print(v)


