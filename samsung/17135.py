
import sys 
from collections import deque 

def copy(orig):
    return deque([ori[:] for ori in orig])

dx = [-1,0,0]
dy = [0,-1,1]
def bow_range(m,ranger,d): 
    for i in range(m):
        ranger[i].append((n-1,i,1))
        q = deque([(n-1,i,1)])
        check = [[True for _ in range(m)] for _ in range(n)]
        while q : 
            x,y,dist = q.popleft()
            if dist ==d :
                break 
            for px,py in zip(dx,dy):
                nx,ny = x+px, y+py 
                if 0<=nx and 0<=ny<m and check[nx][ny] : 
                    check[nx][ny] = False 
                    ranger[i].append((nx,ny,dist+1))
                    q.append((nx,ny,dist+1))
        ranger[i].sort(key= lambda x: (x[2],x[1]))

def get_point(line):
    ret = 0 
    world2 = copy(world)
    bow = [ranger[i] for i in line] 
    for _ in range(n):
        die = [] 
        for b in bow: 
            for position in b : 
                x,y,d = position 
                if world2[x][y] != 0 : 
                    if world2[x][y] == 1:
                        ret +=1 
                        world2[x][y] = -1 
                        die.append((x,y))
                    break 
        for die_position in die : 
            x,y = die_position 
            world2[x][y] = 0 
        world2.pop()
        world2.appendleft([0 for _ in range(m)])
    return ret

def bow(line,cnt,index): 
    if cnt == 3 : 
        global answer
        answer = max(answer,get_point(line))
        
    for i in range(index,m):
        line.append(i)
        bow(line,cnt+1,i+1)
        line.pop()

n,m,d = map(int,sys.stdin.readline().split())
world = deque(list(map(int,sys.stdin.readline().split())) for _ in range(n))
ranger = [[] for _ in range(m)]
answer = 0 
bow_range(m,ranger,d)
bow([],0,0)
print(answer)