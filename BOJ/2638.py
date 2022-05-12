"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""
import sys 
from collections import deque 
def f1(q):
    next= deque() 
    is_change = False 
    while q : 
        x,y = q.popleft()
        for px,py in zip(dx,dy):
            nx,ny = x+px, y+py 
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] : 
                if check[nx][ny] != 0 :
                    check[nx][ny] -= 1 
                    if check[nx][ny] == 0:
                        visit[nx][ny] = False
                        next.append((nx,ny))

                else : 
                    visit[nx][ny] = False 
                    q.append((nx,ny))
    return next
    
n,m = map(int,sys.stdin.readline().split()) 
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
check = [[maps[i][j]*2 for j in range(m)] for i in range(n)]
visit = [[True for _ in range(m)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
start = deque([(0,0),(n-1,m-1),(0,m-1),(n-1,0)])
# f1(start)
answer = 0 
is_end = False 
for ma in maps :
    if any(ma):
        is_end = True 
        break 
while is_end:
    start = f1(start)
    if not start:
        break 
    answer +=1 
print(answer)
