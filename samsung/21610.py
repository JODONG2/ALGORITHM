import sys 
from collections import deque 
n,m = map(int, sys.stdin.readline().split())
world = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
wind = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
direction = [0,(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

cloud = deque([[n-1,0],[n-1,1],[n-2,0],[n-2,1]])

def do_wind(d,s): 
    for c in cloud : 
        c[0] += direction[d][0] * s
        c[0] %= n 
        c[1] += direction[d][1] * s 
        c[1] %= n 

dir = [(1,-1),(-1,1),(1,1),(-1,-1)]
check = [[True for _ in range(n)] for _ in range(n)]

def rain_make_cloud():
    global cloud 
    for x,y in cloud :
        world[x][y] += 1 
        check[x][y] = False 
    # for x,y in cloud : 
    while cloud : 
        x,y = cloud.pop()
        for px,py in dir: 
            nx,ny = x+px, y+py 
            if 0<=nx<n and 0<=ny<n and world[nx][ny] != 0 : 
                world[x][y] += 1 
    
    for x in range(n):
        for y in range(n): 
            if world[x][y] >= 2 and check[x][y]: 
                cloud.append([x,y])
                world[x][y] -= 2 
            elif not check[x][y] : 
                check[x][y] = True  

for d1,s1 in wind : 
    do_wind(d1,s1)
    rain_make_cloud() 

answer =0 
for w in world: 
    answer += sum(w)
print(answer)
