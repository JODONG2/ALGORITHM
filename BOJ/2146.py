import sys 
from collections import deque 
dx = [1,0,0,-1]
dy = [0,1,-1,0]
def grouping(i,j,num):
    visited[i][j] = True 
    next_path = deque()
    maps[i][j] = num 
    q= deque([(i,j)]) 
    while q : 
        x,y = q.popleft() 
        for px,py in zip(dx,dy): 
            nx,ny = x+px, y+py 
            if 0<= nx < n and 0<= ny<n and not visited[nx][ny] :
                if maps[nx][ny] == 1:
                    visited[nx][ny] = True 
                    maps[nx][ny] = num
                    q.append((nx,ny))
                elif maps[nx][ny] == 0:
                    next_path.append((nx,ny,1))
    return next_path

def find_min_bridge():
    ret = 201 
    for island_id, island in enumerate(next): 
        q = deque(island)
        island_id+=1 
        while q : 
            found = False 
            x,y,cost = q.popleft()
            for px,py in zip(dx,dy):
                nx,ny = x+px, y+py 
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and maps[nx][ny] != island_id:
                    if maps[nx][ny] != 0 : 
                        ret = min(ret,cost)
                        found = True 
                        break 
                    else : 
                        visited[nx][ny] = True 
                        q.append((nx,ny,cost+1))
            if found : 
                break 
    return ret 


n = int(sys.stdin.readline())
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)] 
num = 1 
next = deque()
for i in range(n):
    for j in range(n): 
        if maps[i][j] == 1 and not visited[i][j] : 
            next.append(grouping(i,j,num))
            num+=1
visited = [[False for _ in range(n)] for _ in range(n)]
print(find_min_bridge())
