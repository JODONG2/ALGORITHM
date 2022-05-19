import sys 
from collections import deque 
r,c,k = map(int,sys.stdin.readline().split())
# 조사하는곳이 k도 이상이면 끝 
room = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]
wall_cnt = int(input())
wall = [list(map(int,sys.stdin.readline().split())) for _ in range(wall_cnt)] 

heater = {} 
heater_num = 0 
target = []
for i in range(r):
    for j in range(c): 
        if room[i][j] != 0 : 
            if room[i][j] <5 : 
                heater[heater_num] = [2*i,2*j,room[i][j]-1]
                heater_num+=1 
            else : 
                target.append((2*i,2*j))
heater_range = [[0 for _ in range(2*c)] for _ in range(2*r)]
wall_dir = [(-1,0), (0,1)]
for w in wall :
    heater_range[(w[0]-1)*2+wall_dir[w[2]][0]][(w[1]-1)*2+wall_dir[w[2]][1]] = -1 
direction = [(0,1),(0,-1),(-1,0),(1,0)] 
width = [(1,0),(0,1)]
r*=2
c*=2

def wind(heater):
    for key in range(heater_num) :
        check = [[True for _ in range(c)] for _ in range(r)]
        x,y,d = heater[key]
        q = deque()
        q.append((x,y,5))
        while q: 
            x,y,t = q.popleft()
            if t == 0 :
                break 
            succ = True
            nx,ny = x,y 
            for _ in range(2):# 직진
                nx,ny = nx+direction[d][0], ny+direction[d][1] 
                if not(0<=nx< r and 0<=ny<c and heater_range[nx][ny] != -1): 
                    succ = False 
                    break 
            if succ and check[nx][ny]: 
                heater_range[nx][ny] += t
                q.append((nx,ny,t-1))
                check[nx][ny] = False 
            if t == 5 :
                continue 
            succ = True 
            nx,ny = x,y
            for _ in range(2): 
                nx,ny = nx+width[d//2][0],ny+width[d//2][1]
                if not(0<=nx<r and 0<=ny<c and heater_range[nx][ny] != -1):
                    succ= False 
                    break
            if succ :
                for _ in range(2): 
                    nx,ny = nx+direction[d][0], ny+direction[d][1] 
                    if not(0<=nx<r and 0<=ny<c and heater_range[nx][ny] != -1 ): 
                        succ = False 
                        break 
            if succ and check[nx][ny] : 
                heater_range[nx][ny] += t 
                q.append((nx,ny,t-1)) 
                check[nx][ny] = False 
            
            succ = True 
            nx,ny = x,y
            for _ in range(2): 
                nx,ny = nx-width[d//2][0], ny-width[d//2][1] 
                if not(0<=nx<r and 0<=ny<c and heater_range[nx][ny] != -1) : 
                    succ = False 
                    break 
            if succ : 
                for _ in range(2): 
                    nx,ny = nx+direction[d][0], ny+direction[d][1] 
                    if not (0<=nx<r and 0<=ny<c and heater_range[nx][ny] != -1 ):
                        succ = False 
                        break 
            if succ and check[nx][ny] : 
                heater_range[nx][ny] += t 
                q.append((nx,ny,t-1)) 
                check[nx][ny] = False 

dx = [2,0]
dy = [0,2]
lx,ly = [1,0],[0,1]
def temper_avg(heater_range):
    temp_heater_range = [[heater_range[i][j] for j in range(c)] for i in range(r)]
    for i in range(0,r,2): #r *= 2 돼있음
        for j in range(0,c,2): 
            for px,py,cx,cy in zip (dx,dy,lx,ly): 
                nx,ny = i+px, j+py
                wx,wy = i+cx,j+cy 

                if 0<=nx<r and 0<=ny<c and heater_range[wx][wy] != -1 :
                    sub = heater_range[i][j] - heater_range[nx][ny]
                    if sub <= -4 : 
                        sub = abs(sub)
                        temp_heater_range[i][j] += sub//4 
                        temp_heater_range[nx][ny] -= sub//4  
                    elif sub >= 4 : 
                        temp_heater_range[i][j] -= sub//4 
                        temp_heater_range[nx][ny] += sub//4 
    return side(temp_heater_range)

def side(heater_range): 
    
    for i in range(0,r,2):
        if heater_range[i][0] > 0 : 
            heater_range[i][0] -= 1 
        if heater_range[i][c-2] > 0 : 
            heater_range[i][c-2] -= 1
    for j in range(2,c-2,2): 
        if heater_range[0][j] > 0 : 
            heater_range[0][j] -=1 
        if heater_range[r-2][j] > 0 : 
            heater_range[r-2][j] -=1 
    
    return heater_range


heater_range2 = [[0 for _ in range(c)] for _ in range(r)]

for w in wall : 
    heater_range2[(w[0]-1)*2+wall_dir[w[2]][0]][(w[1]-1)*2+wall_dir[w[2]][1]] = -1 
succ = True 
answer = 0 

wind(heater)

while succ and answer<101 : 
    succ = False 
    answer +=1 
    for i in range(0,r,2):
        for j in range(0,c,2): 
            heater_range2[i][j] += heater_range[i][j]

    heater_range2 = temper_avg(heater_range2)

    for x,y in target : 
        if heater_range2[x][y] < k : 
            succ = True 
            break 

print(answer)


"""
[0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1]
[0, 2, 2, 2, 7, 2, 2, 2]
[0, 0, 3, 4, 7, 4, 3, 0]
[0, 0, 3, 4, 7, 4, 3, 0]
[0, 2, 2, 2, 7, 2, 2, 2]
[1, 1, 1, 1, 1, 1, 1, 1]

[0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 2, 1, 1, 0]
[0, 2, 2, 3, 4, 3, 2, 1]
[0, 0, 3, 4, 7, 4, 3, 0]
[0, 0, 3, 4, 7, 4, 3, 0]
[0, 2, 2, 3, 4, 3, 2, 1]
[0, 0, 0, 0, 1, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0]
[0, 2, 2, 2, 5, 2, 2, 0]
[0, 2, 4, 6, 7, 6, 4, 2]
[0, 2, 5, 9, 12, 9, 5, 0]
[0, 2, 5, 9, 12, 9, 5, 0]
[0, 2, 4, 5, 7, 5, 4, 2]
[0, 0, 0, 1, 3, 1, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1]
[0, 2, 2, 2, 7, 2, 2, 2]
[0, 0, 3, 4, 7, 4, 3, 0]
[0, 0, 3, 4, 7, 4, 3, 0]
[0, 2, 2, 2, 7, 2, 2, 2]
[1, 1, 1, 1, 1, 1, 1, 1]


7 8 1
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0


7 8 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0

7 8 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1
4 2 1

7 8 1
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
3
5 4 0
4 4 1 
5 6 0 
"""
