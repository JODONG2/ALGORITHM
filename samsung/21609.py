
"""
 초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다. 
 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현한다. 
 검은색 블록은 -1, 무지개 블록은 0으로 표현한다. 
 (i, j)는 격자의 i번 행, j번 열을 의미하고, 
 |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸 (r1, c1)과 (r2, c2)를 인접한 칸이라고 한다.
 블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 
 일반 블록의 색은 모두 같아야 한다. 
 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 
 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. 
 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
크기가 가장 큰 블록 그룹을 찾는다.
    그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
격자에 중력이 작용한다.
격자가 90도 반시계 방향으로 회전한다.
다시 격자에 중력이 작용한다.

"""

import sys 

n,m = map(int, sys.stdin.readline().split()) 
world = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
rain_position = []

from collections import deque 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0 
def search_max(n): 
    global answer 
    q = deque()
    check = [[True for _ in range(n)] for _ in range(n)]
    ret = []
    maxi_rain = 0 
    succ = False 
    rain_position = [] 
    for i in range(n):
        for j in range(n):
            if world[i][j] != 0 and world[i][j] != -1 and world[i][j] != -2 and check[i][j] : 
                q.append((i,j)) 
                check[i][j] = False 
                save = deque()
                save.append((i,j))
                rain_cnt = 0 
                while q:
                    x,y = q.popleft()
                    for px,py in zip(dx,dy): 
                        nx,ny = x+px,y+py 
                        if 0<=nx<n and 0<=ny<n and check[nx][ny] and (world[i][j] == world[nx][ny] or world[nx][ny] == 0) : 
                            q.append((nx,ny)) 
                            save.append((nx,ny)) 
                            check[nx][ny] = False 
                            if world[nx][ny] == 0 :
                                rain_cnt+=1 
                                rain_position.append((nx,ny))
                len_save = len(save)
                if len_save >= 2 : 
                    succ = True 
                    if len_save > len(ret) : 
                        ret = [s for s in save]
                        maxi_rain = rain_cnt
                    elif len_save == len(ret) and maxi_rain <= rain_cnt: 
                        ret = [s for s in save]
                        maxi_rain = rain_cnt
                for rx,ry in rain_position : 
                    check[rx][ry] = True
    if succ : 
        answer += len(ret) ** 2 
        for x,y in ret : 
            world[x][y] = -2 

    return succ 

def gravity_d(n):
    for i in range(n):
        height = n-1 
        for j in range(n-1,-1,-1): 
            if world[j][i] == -2 :
                continue 
            elif world[j][i] == -1 : 
                height = j -1  
            else :
                world[height][i], world[j][i] = world[j][i],world[height][i]
                height -= 1 

def rotate(n): 
    ret = [[0 for _ in range(n)] for _ in range(n)] 
    global world 
    for i in range(n):
        for j in range(n): 
            ret[n-1-j][i] = world[i][j]
    world = ret 

while search_max(n): 
    gravity_d(n)
    rotate(n)
    gravity_d(n) 
    # for w in world:
    #     print(w)
print(answer)

"""
5 1 
1 1 1 1 1
-1 -1 -1 -1 1 
1 1 1 1 1 
1 -1 -1 -1 -1 
1 1 1 1 1

5 2 
1 1 1 1 1
-1 -1 -1 -1 1 
2 2 -1 1 1 
2 -1 -1 -1 -1 
2 2 2 2 2

5 2
1 -1 2 2 2
1 -1 2 -1 2 
1 -1 -1 -1 2 
1 -1 1 -1 2 
1 1 1 -1 2 

5 2
1 -1 2 2 2
1 -1 2 -1 2 
1 -1 -1 -1 2 
1 -1 1 -1 2 
0 1 1 -1 2 

4 2
1 1 1 1
2 2 2 1
2 1 1 1
2 2 2 2

5 2 
1 -1 2 2 2
1 -1 2 -1 2 
1 -1 -1 -1 2 
1 -1 2 -1 2 
1 1 1 -1 2

5 2 
1 -1 2 2 2
1 -1 2 -1 2 
1 -1 -1 -1 2 
1 -1 2 -1 2 
1 1 1 -1 2

5 2
2 2 2 2 2
2 2 2 2 2
2 2 2 2 2
2 2 2 2 2
2 2 2 2 2

6 3
1 1 1 0 0 0
1 1 1 0 0 0
1 1 3 0 0 0
0 0 0 2 2 2
0 0 0 2 2 2
0 0 0 2 2 2
"""
                    

