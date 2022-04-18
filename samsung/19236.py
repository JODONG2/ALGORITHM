"""
첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다. 
물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다. 
방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.
상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 출력한다.

"""
input_data = [list(map(int,input().split())) for _ in range(4)]
fish_dic = {} 
space = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4) : 
    for j in range(0,8,2) :
        space[i][j//2] = input_data[i][j] 
        fish_dic[input_data[i][j]] = [i,j//2,input_data[i][j+1] - 1]

# 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗
direction = [(-1,0),(-1,-1), (0,-1), (1,-1),(1,0),(1,1),(0,1),(-1,1)]



def copy_dic(ori):
    ret = {} 
    for key in ori.keys():
        ret[key] = ori[key][:]
    return ret 

def copy_space(ori):
    temp = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i][j] = ori[i][j] 
    return temp

from collections import deque 

def fish_move(ts1,tfk1): 
    ts = copy_space(ts1)
    tfk = copy_dic(tfk1)
    for key in range(1,17): 
        if tfk.get(key):
            x,y,d = tfk[key]
            nx,ny = x+direction[d][0], y+direction[d][1]
            succ = False 
            for _ in range(8): 
                if 0<=nx<4 and 0<=ny<4 and ts[nx][ny] != -1 :
                    succ = True 
                    break 
                d+=1
                nx,ny = x+direction[d%8][0], y+direction[d%8][1]
            if succ:
                if tfk.get(ts[nx][ny]):
                    tfk[ts[nx][ny]][0], tfk[ts[nx][ny]][1] = x,y
                tfk[key][0], tfk[key][1], tfk[key][2] = nx,ny,d%8
                ts[x][y],ts[nx][ny] = ts[nx][ny],ts[x][y]
    return ts,tfk

# space, fish_dic = fish_move(space,fish_dic) # first move 

def shark_move(shark_position,space): 
    x,y,d = shark_position
    ret = 0 
    if (x,y) == (0,0):
        del fish_dic[space[0][0]]
        ret += space[0][0]
        space[0][0] = -1
        temp_space,temp_fish_dic = fish_move(space,fish_dic)
        
    q = deque([(x,y,d,temp_space,ret,temp_fish_dic)]) 
    while q :
        x,y,d,temp_space,point, temp_fish_dic= q.popleft()
        if ret<point : 
            ret= point 
        temp_space[x][y] = 0 # 이동 
        px,py = direction[d]
        nx,ny = x,y
        while 0<=nx + px<4 and 0<=ny+py<4 : 
            nx,ny = nx+px,ny+py
            if 0<=nx<4 and 0<=ny<4 and temp_space[nx][ny] != 0 :
                key = temp_space[nx][ny] 
                fx,fy,fd = temp_fish_dic[key]
                nd=fd 
                del temp_fish_dic[key]
                temp_space[nx][ny] = -1
                ts,tfk = fish_move(temp_space,temp_fish_dic)
                q.append((nx,ny,nd,ts,point+key, tfk))
                temp_space[nx][ny] = key 
                temp_fish_dic[key] = [fx,fy,fd]
    return ret 

shark_position = [0,0,fish_dic[space[0][0]][2]]
print(shark_move(shark_position,space))




"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2

16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4
"""