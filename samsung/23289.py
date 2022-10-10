import sys 
r,c,k = map(int,sys.stdin.readline().split())
room = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]
heater = {} 
heater_num = 0 
target = []
for i in range(r): 
    for j in range(c): 
        if room[i][j] != 0 :
            if room[i][j] < 5 : 
                heater[heater_num] = [i,j,room[i][j]-1]
                room[i][j] = 0 
                heater_num += 1 
            elif room[i][j] == 5 : 
                target.append((i,j)) 
                room[i][j] = 0 

wall_cnt = int(input()) 
# wall = [list(map(int,sys.stdin.readline().split())) for _ in range(wall_cnt)]
wall_room = [[-1 for _ in range(c)] for _ in range(r)]
for _ in range(wall_cnt): 
    x,y,t = map(int,sys.stdin.readline().split())

    if t == 0 : t= 2
    elif t == 1 : t= 0  
    wall_room[x-1][y-1] = t

direction = [(0,1),(0,-1),(-1,0),(1,0)]
width = [(1,0),(0,1)]
heater_range = [[0 for _ in range(c)] for _ in range(c) ]
#TODO: 1,3,5,7,9
#TODO: x , 0, 1~3 , 4~8, 9~15
#TODO: 0 , 1, 2   , 3,   4 
from collections import deque 

def heater_range_make(heater,wall_room): 
    for key in range(heater_num):
        x,y,d= heater[key] 
        q = deque() 
        check = [[True for _ in range(c)] for _ in range(r)]
        q.append((x,y,5))
        while q : 
            x,y,t = q.popleft() 
            if t == 0 : 
                break 
            nx,ny = x+direction[d][0], y+direction[d][1]
            if 0<=nx<r and 0<=ny<c and check[nx][ny] :
                if wall_room[x][y] != d and d - wall_room[nx][ny] != 1  : 
                    if t == 5 :  # 온풍기 +1 칸 처리 
                        q.append((nx,ny,t))
                        heater_range[nx][ny] += t 
                        check[nx][ny] = False 
                        continue 
                    heater_range[nx][ny] += t
                    q.append((nx,ny,t-1)) 
                    check[nx][ny] = False
            nx1,ny1 = x+direction[d][0]+width[d//2][0], y+direction[d][0]+width[d//2][1]
            wx,wy = x+width[d//2][0],y+width[d//2][1]
            if 0<=nx1<r and 0<=ny1<c and 0<=wx<r and 0<=wy<c and check[nx1][ny1] and wall_room[wx][wy] != d and wall_room[nx1][ny1] : 
                # (x, y)에서 (x, y+1)로 바람이 이동할 수 있으려면 (x, y)와 (x, y+1) 사이에 벽이 없어야 한다. 
                # 마지막으로 (x, y)에서 (x+1, y+1)로 바람이 이동할 수 있으려면, (x, y)와 (x+1, y), (x+1, y)와 (x+1, y+1) 사이에 벽이 없어야 한다.
                q.append((nx1,ny1,t-1))
                check[nx1][ny1] = False 
                heater_range[nx1][ny1] += t-1 

                
                

    # for key in range(heater_num) : 
    #     x,y,d = heater[key] 
    #     heater_range[key] = [] 
    #     for i in range(5): 
    #         nx,ny = x+direction[d][0]-width[d//2][0]*i, y+direction[d][1] - width[d//2][1]*i
    #         nx2,ny2 = x+direction[d][0]+width[d//2][0]*i, y+direction[d][1]-width[d//2][1]*i 
    #         if i == 0 : 
    #             heater_range[key].append((nx,ny,5-i))
    #         else :
    #             bx,by,alpha = heater_range[key][(i-1)*(i-1)][0] 
    #             new_x,new_y = bx+direction[d][0]+width[d//2][0], by+direction[d][1]+width[d//2][1] 
    #             if 0<=new_x<r and 0<=new_y<c and wall_room[bx][by]
    #             for bx,by,alpha in heater_range[key][(i-1)*(i-1) :] :
    #                 new_x,new_y = bx+direction[d][0],by+direction[d][1]
    #                 if 0<=new_x<r and 0<=new_y<c :
    #                     if wall_room[bx][by] == d or d - wall_room[new_x][new_y] != 1:
    #                         heater_range[key].append((new_x,new_y,0))
    #                     else : 
    #                         heater_range[key].append((new_x,new_y,5-i))

heater_range_make(heater,wall_room) 

for i in range(heater_num):
    for x,y,d in heater_range[i] : 
        room[x][y] += d 

for r in room:
    print(r)

print(heater)
print(target)
print(heater_range)