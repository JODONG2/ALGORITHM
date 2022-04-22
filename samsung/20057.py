"""
오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.

"""

#TODO: move() -> 토네이도 이동 
#TODO: 모래 날리기 -> 
import sys 
n = int(sys.stdin.readline()) 
world = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
position = [n//2, n//2]

to_dir = [(0,-1), (1,0), (0,1), (-1,0)]

sand_dir = [(-2,0,0.02), (-1,-1, 0.1), (-1,0,0.07), (-1,1,0.01), (0,-2,0.05), (1,-1,0.1), (1,0,0.07), (1,1,0.01),(2,0,0.02)]
# 좌가 기준
# 하 = x,y -> -y,x 
# 우 = x,y -> x,-y 
# 상 = x,y -> y,x 
#left에서 멈춤 
def diffusion(position,world,d): 
    ret = 0 
    x,y = position
    moving = 0 
    for px,py,per in sand_dir :

        if d==1 : #하
            px,py = -py, px 
        elif d== 2: #우 
            px,py = px,-py 
        elif d==3: #상 
            px,py = py, px 

        nx,ny = x+px,y+py
        sand = int(world[x][y]*per)
        moving+=sand
        
        if 0<= nx <n and 0<= ny <n : 
            world[nx][ny] += sand 
        else : 
            ret += sand 

    tx,ty = to_dir[d]
    nx,ny = x+tx, y+ty 
    if 0<=nx<n and 0<=ny<n : # a위치 
        world[nx][ny] += world[x][y] - moving 
        world[x][y] = 0 
    else : 
        ret += world[x][y] - moving
        world[x][y] = 0 

    return ret 

def move(position) : 
    limit = 0 
    ret = 0 
    while limit < n : 
        limit +=1
        if limit >= n :
            limit-=1
        for _ in range(limit) : #좌 
            position[0]+= to_dir[0][0] 
            position[1]+= to_dir[0][1]
            ret += diffusion(position,world,0)
        if limit == n-1: 
            break 
        for _ in range(limit): #하
            position[0]+= to_dir[1][0]
            position[1]+= to_dir[1][1]
            ret += diffusion(position,world,1)
        limit+=1 
        for _ in range(limit) : #우 
            position[0]+= to_dir[2][0] 
            position[1]+= to_dir[2][1] 
            ret += diffusion(position,world,2)
        for _ in range(limit) : #상 
            position[0]+= to_dir[3][0] 
            position[1]+= to_dir[3][1] 
            ret += diffusion(position,world,3)        
    return ret 

print(move(position))