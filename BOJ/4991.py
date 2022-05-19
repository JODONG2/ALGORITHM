"""
7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
"""
import sys
from collections import deque 
dx= [0,1,-1,0]
dy= [1,0,0,-1]

def bfs(start,cnt,num): 
    distance = [-1 for _ in range(cnt)] 
    distance[num] = 0 
    cnt -= 1 
    q =deque([start]) 
    visit = [[True for _ in range(w)] for _ in range(h)]
    visit[start[0]][start[1]] = False 
    while q : 
        x,y,d = q.popleft()
        for px,py in zip(dx,dy): 
            nx,ny = x+px, y+py 
            if 0<=nx<h and 0<=ny<w and maps[nx][ny] != 'x' and visit[nx][ny] : 
                visit[nx][ny] = False 
                if maps[nx][ny] != 'o' and maps[nx][ny] != '.': 
                    distance[maps[nx][ny]] = d+1 
                    cnt -= 1 
                    if cnt ==-1 : 
                        return distance
                elif maps[nx][ny] == 'o' : 
                    distance[num] = d+1 
                    cnt -=1 
                    if cnt == -1: 
                        return distance
                q.append((nx,ny,d+1))
    return -1 

short_dist = float('inf')
last = -1 
first = -1
def find_short_distance(dist,cnt,sum_dist,now,visit): 
    global short_dist 
    if len(visit) == cnt : 
        if short_dist > sum_dist : 
            short_dist = sum_dist 
    if sum_dist >= short_dist : 
        return 
    for i in range(cnt):
        if not visit : 
            visit.append(i)
            find_short_distance(dist, cnt , dist[i][i] , i , visit)
            visit.pop()
        elif not i in visit : 
            visit.append(i)
            find_short_distance(dist,cnt,sum_dist+dist[now][i],i,visit)
            visit.pop()

def start_first_last(start,dest): 
    q = deque(start) 
    visit = [[True for _ in range(w)] for _ in range(h)]
    while q : 
        x,y,d=  q.popleft()
        for px,py in zip(dx,dy): 
            nx,ny = x+px, y+py 
            if 0<=nx<h and 0<=ny<w and visit[nx][ny] : 
                if maps[nx][ny] == dest : 
                    return d +1 
                q.append((nx,ny,d+1))
                visit[nx][ny] = False 
    return -1 
answer_list = []
while True:
    w,h = map(int,sys.stdin.readline().split())
    if (w,h) == (0,0) :
        break 
    maps = [list(sys.stdin.readline()[:-1]) for _ in range(h)]
    cnt = 0 
    dusts = [] 
    dist = [] 
    for i in range(h):
        for j in range(w): 
            if maps[i][j] == 'o' : 
                start = [(i,j,0)]
            elif maps[i][j] == '*' : 
                maps[i][j] = cnt
                cnt+=1 
                dusts.append((i,j,0))
    answer = 0
    for num,dust in enumerate(dusts): 
        dist.append((bfs(dust,cnt,num)))
        if dist[-1] == -1 : 
            answer = -1 
            break 
    if answer != -1 :
        find_short_distance(dist,cnt,0,0,[])
        print(short_dist)
        answer_list.append(short_dist)
    else:
        print(answer)
        answer_list.append(-1)
    short_dist = float('inf')
"""
3 3
...
.o*
***

5 5
*...*
.....
..o..
*...*
.....
"""