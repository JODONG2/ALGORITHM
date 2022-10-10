from collections import deque 
def f1(): 
    visited = [[float('inf') for _ in range(n)] for _ in range(n)]
    q = deque() 
    q.append((0,0,0))
    while q : 
        x, y, cost = q.popleft() 
        for px,py in zip(dx,dy):
            nx,ny = x+px,y+py 
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] > cost : 
                visited[nx][ny] = cost
                if q and q[0][2] > cost+maps[nx][ny]: 
                    q.appendleft((nx,ny,cost+maps[nx][ny]))
                    continue 
                q.append((nx,ny,cost+maps[nx][ny]))
    return visited[-1][-1]
    
dx = [0,1,-1,0]
dy = [1,0,0,-1]
tc = int(input())
for t in range(1,tc+1):
    n = int(input())
    maps = [list(map(int,input())) for _ in range(n)] 
    print(f'#{t} {f1()}')




#1 17
#2 96
#3 49
#4 39
#5 49
#6 1
#7 28
#8 45
#9 59
#10 64