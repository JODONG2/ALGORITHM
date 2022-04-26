import sys 
from collections import deque 
n,m,k = map(int,sys.stdin.readline().split())
world = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# 시작은 동쪽방향 -> 
#위쪽이 북쪽  :  동쪽이 오른쪽
direction = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0

dice1= deque([2,1,5,6]) # 상하 
dice2= deque([4,1,3,6]) # 좌우
#바닥 index = 3
#위 index = 1 
def left(dice1,dice2):
    dice1[1] = dice2[2]
    dice1[3] = dice2[0] 
    dice2.append(dice2.popleft())

def right(dice1,dice2): 
    dice1[1] = dice2[0]
    dice1[3] = dice2[2]
    dice2.appendleft(dice2.pop())

def down(dice1,dice2):
    dice2[1] = dice1[0] 
    dice2[3] = dice1[2]
    dice1.appendleft(dice1.pop())

def up(dice1,dice2):
    dice2[1] = dice1[2] 
    dice2[3] = dice1[0] 
    dice1.append(dice1.popleft())
#우상하좌
world_point = [[0 for _ in range(m)] for _ in range(n)]
def get_point(x,y):
    if world_point[x][y] != 0 : 
        return world_point[x][y]
    cnt = 1
    check = [[True for _ in range(m)] for _ in range(n)]
    check[x][y] = False 
    num = world[x][y]
    q = deque([(x,y)])
    while q : 
        nx,ny = q.popleft()
        for px,py in direction:
            new_x,new_y= nx+px,ny+py 
            if 0<=new_x<n and 0<=new_y<m and check[new_x][new_y] and world[new_x][new_y] == num : 
                cnt +=1 
                q.append((new_x,new_y))
                check[new_x][new_y] = False 
    world_point[x][y] = num*cnt
    return num*cnt

def move(x,y,d):
    nx,ny = x+direction[d][0] , y+direction[d][1]
    #
    if not(0<=nx<n and 0<=ny<m) : 
        d+=2
        d%=4 
        nx,ny = x+direction[d][0], y+direction[d][1]
    if d == 0 : 
        right(dice1,dice2)    
    elif d==1 :
        down(dice1,dice2)
    elif d==2 : 
        left(dice1,dice2)
    elif d==3:
        up(dice1,dice2)

    if world[nx][ny] < dice1[3] : 
        d+=1 
        d%=4
    elif world[nx][ny] > dice1[3] : 
        d-=1
        d%=4
    point = get_point(nx,ny)
    return nx,ny,d,point

if __name__ == "__main__": 
    answer = 0 
    x,y,d = 0,0,0
    for _ in range(k):
        x,y,d,point = move(x,y,d)
        answer += point 
    print(answer)