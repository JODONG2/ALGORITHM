from collections import deque 
import sys 
n,q = map(int,sys.stdin.readline().split()) 
n2 = 2**n
world = [list(map(int,sys.stdin.readline().split())) for _ in range(n2)]
command = list(map(int,sys.stdin.readline().split())) 

def spin_90(SIZE) :
    if SIZE == 0 : 
        return 
    global world 
    temp = [[0 for _ in range(n2)] for _ in range(n2)]
    s2 = 2**SIZE
    for i in range(0,(n2), (s2)) : 
        for j in range(0,(2**n), (s2)) : 
            for i2 in range(s2):
                for j2 in range(s2):
                    temp[i+j2][j+(s2-1)-i2]=world[i+i2][j+j2]
    world=temp

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def melting() :
    global world
    temp = [world[i][:] for i in range(n2)] 
    for i in range(n2):
        for j in range(n2) : 
            if world[i][j] == 0 : 
                continue 
            cnt = 0 
            for pi,pj in zip(dx,dy): 
                ni,nj = i+pi, j+pj 
                if (0<=ni<n2 and 0<=nj<n2 and world[ni][nj] != 0) : 
                    cnt += 1 
            if cnt < 3 : 
                temp[i][j] -= 1 
    world = temp
    # return temp 


def counting(world):
    check = [[True for _ in range(n2)] for _ in range(n2)]
    maxi = 0 
    all_thing = 0     
    for x in range(n2):
        for y in range(n2): 
            all_thing+= world[x][y] 
            if not check[x][y] or world[x][y] == 0 :
                continue 
            check[x][y] = False 
            cnt = 1 
            q = deque()
            q.append((x,y)) 
            while q: 
                tx,ty = q.popleft()
                for px,py in zip(dx,dy): 
                    nx,ny = tx+px, ty+py 
                    if 0<=nx<n2 and 0<=ny<n2 and check[nx][ny] and world[nx][ny] != 0 : 
                        q.append((nx,ny)) 
                        check[nx][ny] = False 
                        cnt +=1 
            if maxi < cnt : 
                maxi= cnt 
    return all_thing, maxi 

for c in command:
    spin_90(c)
    melting()
a1,a2= counting(world)
print(a1)
print(a2)



        
"""

3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
2
"""