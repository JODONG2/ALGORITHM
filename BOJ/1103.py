import sys 
from collections import deque 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(start,world,n,m):
    q = deque(start)
    time = 1
    check = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        x,y,time,visit = q.popleft() 
        for px,py in zip(dx,dy):
            nx,ny = x+(px*world[x][y]), y+(py*world[x][y])
            if 0<=nx<n and 0<=ny<m and world[nx][ny] != 'H': 
                if (nx,ny) in visit :
                    return -1 
                if check[nx][ny] >= time+1 :
                    continue 
                check[nx][ny] = time+1 
                visit.append((nx,ny))
                q.append((nx,ny,time+1,visit[:]))
                visit.pop()
    return time 
n,m = map(int,sys.stdin.readline().split()) 
world = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if world[i][j]!='H':
            world[i][j] = int(world[i][j])

start = [(0,0,1,[0,0])]
print(bfs(start,world,n,m))