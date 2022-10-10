
import sys 
from collections import deque 
dx = [0,-1,0,1]
dy = [-1,0,1,0] 
def bfs(x,y): # 가생이만 넣을거임 
    q = deque([x,y,pool[x][y]])
    origin_h = pool[x][y]
    while q : 
        x,y,h = q.popleft()
        next_h = 10
        temp = [] 
        for px,py in zip(dx,dy):
            nx,ny = x+px, y+py 
            if 0<=nx<n and 0<=ny<m and check[nx][ny]:
                if pool[nx][ny] >= h and pool[nx][ny] < next_h: 
                    next_h = pool[nx][ny]
                    check[nx][ny] = False 
                temp.append((nx,ny))
        if next_h == 10:
            next_h = h 
        for nx,ny in temp : 
            q.append((nx,ny,next_h))

    
            


n,m = map(int,sys.stdin.readline().split())
check = [[True for _ in range(m)] for _ in range(n)] 
pool = [list(map(int,list(sys.stdin.readline()[:-1]))) for _ in range(n)]
bfs(pool,check)

"""

5 5
55515
53121
54445
51115
55555


55555
51115
44444
51115
53335

->10 
"""